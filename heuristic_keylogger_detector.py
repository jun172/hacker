#!/usr/bin/env python3
"""
heuristic_keylogger_detector.py
- ヒューリスティックで「怪しいプロセス」を検知してログ＋通知する簡易ツール
- 防御目的・自環境での検証用。商用運用には向きません。
"""

import os
import sys
import time
import json
import hashlib
import logging
from datetime import datetime
from pathlib import Path

import psutil

# Optional: webhook通知
try:
    import requests
except Exception:
    requests = None

# Optional: desktop notification (plyer)
try:
    from plyer import notification
except Exception:
    notification = None

# ---------- 設定（必要に応じて編集） ----------
SCAN_INTERVAL = 5            # 秒
LOG_FILE = "keylogger_detector_log.jsonl"
BASELINE_FILE = "process_baseline.json"
WHITELIST_HASHES = {}       # {"/path/to/bin": "sha256hex", ...}  手動で埋めるか初回生成
SUSPICIOUS_NAMES = [
    "keylogger", "keylog", "klg", "keyboardhook", "spy", "logger", "klogger",
    "winlogon64", "xlogger"  # 参考用。実際の名前は環境に合わせて調整
]
SUSPICIOUS_PATH_KEYWORDS = ["temp", "tmp", "appdata", "localappdata", "download", "/tmp"]

# 外部送信を検知するための接続ポートブラックリスト（必要に応じて）
SUSPICIOUS_REMOTE_PORTS = [80, 443]  # ただし正当なHTTP通信もあるため注意

# Webhook（Slack等）に通知したい場合はURLを入れる（任意）
WEBHOOK_URL = None  # "https://hooks.slack.com/services/xxx/yyy/zzz"

# 最初のベースラインを自動保存するか
AUTO_SAVE_BASELINE = True
# --------------------------------------------------

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def sha256_of_file(path: str) -> str:
    try:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return ""


def is_path_suspicious(exec_path: str) -> bool:
    if not exec_path:
        return False
    p = exec_path.lower()
    for kw in SUSPICIOUS_PATH_KEYWORDS:
        if kw in p:
            return True
    return False


def name_is_suspicious(name: str) -> bool:
    if not name:
        return False
    n = name.lower()
    for s in SUSPICIOUS_NAMES:
        if s in n:
            return True
    return False


def has_remote_connections(proc: psutil.Process) -> bool:
    try:
        for c in proc.connections(kind='inet'):
            if c.raddr:
                # raddr is (ip, port)
                # 単純に外向きのコネクションがあるかだけ見る
                return True
    except Exception:
        pass
    return False


def notify(title: str, message: str):
    logging.warning(f"NOTIFY: {title} - {message}")
    # Desktop notification
    if notification:
        try:
            notification.notify(title=title, message=message, app_name="KeyloggerDetector")
        except Exception:
            pass
    # Webhook (Slack) if configured
    if WEBHOOK_URL and requests:
        try:
            payload = {"text": f"*{title}*\n{message}"}
            requests.post(WEBHOOK_URL, json=payload, timeout=5)
        except Exception:
            pass


def log_event(event: dict):
    event["detected_at"] = datetime.utcnow().isoformat() + "Z"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")
    logging.info("Logged event: %s", event.get("summary", "<no-summary>"))


def build_baseline():
    baseline = {}
    for p in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            exe = p.info.get('exe') or ""
            if exe and os.path.isfile(exe):
                h = sha256_of_file(exe)
                baseline[exe] = h
        except Exception:
            continue
    return baseline


def load_baseline():
    if os.path.exists(BASELINE_FILE):
        try:
            with open(BASELINE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_baseline(baseline: dict):
    with open(BASELINE_FILE, "w", encoding="utf-8") as f:
        json.dump(baseline, f, indent=2)


def analyze_process(p: psutil.Process, baseline_hashes: dict):
    info = {}
    try:
        info['pid'] = p.pid
        info['name'] = p.name()
        info['exe'] = p.exe() if p.exe() else ""
    except Exception:
        return None

    reasons = []
    # 1) suspicious name
    if name_is_suspicious(info['name']):
        reasons.append("suspicious_name")

    # 2) suspicious path
    if is_path_suspicious(info['exe']):
        reasons.append("suspicious_path")

    # 3) not in baseline hash
    if info['exe']:
        h = sha256_of_file(info['exe'])
        baseline_h = baseline_hashes.get(info['exe'])
        if baseline_h and baseline_h != h:
            # file changed
            reasons.append("exec_changed")
        elif not baseline_h:
            # new executable not in baseline
            reasons.append("not_in_baseline")
        info['sha256'] = h

    # 4) remote connections
    try:
        if has_remote_connections(p):
            reasons.append("remote_connections")
    except Exception:
        pass

    if reasons:
        info['reasons'] = reasons
        info['summary'] = f"Suspicious process {info['name']} (pid={info['pid']}) reasons={reasons}"
        return info
    return None


def main_loop():
    # load or build baseline
    baseline = load_baseline()
    if not baseline and AUTO_SAVE_BASELINE:
        logging.info("No baseline found — building baseline from current processes...")
        baseline = build_baseline()
        save_baseline(baseline)
        logging.info("Baseline saved to %s (count=%d)", BASELINE_FILE, len(baseline))

    seen_pids = set()
    while True:
        try:
            current_pids = set(psutil.pids())
            new_pids = current_pids - seen_pids
            for pid in sorted(new_pids):
                try:
                    p = psutil.Process(pid)
                except Exception:
                    continue
                result = analyze_process(p, baseline)
                if result:
                    # log + notify
                    log_event(result)
                    notify("Suspicious process detected", result['summary'])
                # mark seen
                seen_pids.add(pid)
            # also periodically check existing processes for new network connections or path changes
            for pid in list(seen_pids):
                if not psutil.pid_exists(pid):
                    seen_pids.discard(pid)
            time.sleep(SCAN_INTERVAL)
        except KeyboardInterrupt:
            logging.info("Exiting by user")
            break
        except Exception as e:
            logging.exception("Main loop error: %s", e)
            time.sleep(5)


if __name__ == "__main__":
    main_loop()
