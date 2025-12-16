#!/usr/bin/env python3
"""
find_flag.py

使い方:
  # 必要なら pip install requests
  # 例（ENCにはブラウザからコピーしたURLエンコード済み connect.sid を入れる）
  python3 find_flag.py --cookie-enc "s%3A6xZQ..."

オプション:
  --cookie-enc  URLエンコード済み connect.sid を渡す（優先）
  --cookie-dec  デコード済み（s:xxxxx.yyyyy）形式の connect.sid を渡す
  --base-url    ベース URL (デフォルト http://209.38.236.227:30669)
  --save-dir    取得ファイルの保存先 (デフォルト /tmp/ruins_dump)
"""

import argparse
import os
import re
import sys
import urllib.parse
import base64
import codecs
from pathlib import Path

try:
    import requests
except Exception:
    print("このスクリプトは requests が必要です。インストール: pip install requests")
    sys.exit(1)

FLAG_PATTERNS = [
    re.compile(r"FLAG\{[^}]+\}"),
    re.compile(r"CTF\{[^}]+\}"),
    re.compile(r"flag\{[^}]+\}"),
    re.compile(r"[Ff][Ll][Aa][Gg][:]\s*[A-Za-z0-9_\-]{8,}"),
]

BASE64_CAND_RE = re.compile(r"[A-Za-z0-9+/=]{20,}")

URLS = [
    "/", "/api/notes", "/note?id=1", "/login", "/robots.txt", "/sitemap.xml"
]

def try_rot13(s: str) -> str:
    try:
        return codecs.decode(s, "rot_13")
    except Exception:
        return ""

def try_reverse(s: str) -> str:
    return s[::-1]

def decode_base64_candidate(s: str):
    # try to base64-decode a candidate with padding fixes
    for pad in ("", "=", "==", "==="):
        try:
            b = base64.b64decode(s + pad, validate=True)
            try:
                return b.decode("utf-8", errors="ignore")
            except Exception:
                return str(b)
        except Exception:
            continue
    return None

def search_flags(text: str):
    found = []
    for p in FLAG_PATTERNS:
        for m in p.findall(text):
            found.append(m)
    return list(dict.fromkeys(found))  # unique preserve order

def find_base64_strings(text: str):
    return BASE64_CAND_RE.findall(text)

def analyze_text(name: str, text: str):
    results = {"name": name, "status": [], "flags": []}

    # direct search
    flags = search_flags(text)
    if flags:
        results["flags"].extend(flags)

    # reversed search
    rev = try_reverse(text)
    flags = search_flags(rev)
    if flags:
        results["flags"].extend(flags)

    # rot13 search
    rot = try_rot13(text)
    flags = search_flags(rot)
    if flags:
        results["flags"].extend(flags)

    # try reversing + rot13
    rot_rev = try_rot13(rev)
    flags = search_flags(rot_rev)
    if flags:
        results["flags"].extend(flags)

    # search base64-like strings and try decode
    b64s = find_base64_strings(text)
    for cand in set(b64s):
        dec = decode_base64_candidate(cand)
        if dec:
            # search flags in decoded
            f = search_flags(dec)
            if f:
                results["flags"].extend(f)
            # also try rot13/reverse on decoded
            f = search_flags(try_rot13(dec))
            if f:
                results["flags"].extend(f)
            f = search_flags(try_reverse(dec))
            if f:
                results["flags"].extend(f)
    results["flags"] = list(dict.fromkeys(results["flags"]))
    return results

def save_file(path: Path, content: bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--cookie-enc", help="URLエンコード済み connect.sid をそのまま渡す (例 s%%3A...)", default=None)
parser.add_argument("--cookie-dec", help="デコード済み connect.sid (s:... 形式)", default=None)
parser.add_argument("--base-url", help="ベース URL (例 http://209.38.236.227:30669)", default="http://209.38.236.227:30669")
parser.add_argument("--save-dir", help="取得ファイルの保存先", default="/tmp/ruins_dump")


    session = requests.Session()
    session.headers.update({"Origin": "http://localhost:3000", "User-Agent": "flag-finder/1.0"})

    # Prepare cookie: prefer encoded if provided
    cookie_name = "connect.sid"
    if args.cookie_enc:
        # send encoded as-is in header; requests will not auto-encode cookie value if we manually set header,
        # but better to set via cookie jar with decoded value usually. We'll try both ways below.
        cookie_enc = args.cookie_enc
        cookie_dec = urllib.parse.unquote(cookie_enc)
    elif args.cookie_dec:
        cookie_dec = args.cookie_dec
        cookie_enc = urllib.parse.quote(cookie_dec, safe='')
    else:
        print("エラー: --cookie-enc か --cookie-dec のどちらかを指定してください。")
        parser.print_help()
        sys.exit(1)

    print("[*] cookie (decoded form hidden). Use your own cookie; do not paste it publicly.")

    save_dir = Path(args.save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)

    found_any = []

    # Try two methods: set cookie jar with decoded value, and raw header with encoded.
    # 1) cookie jar (decoded)
    session.cookies.set(cookie_name, cookie_dec, domain=urllib.parse.urlparse(args.base_url).hostname)
    print("[*] Using cookie jar with decoded value and requests session.")

    for u in URLS:
        url = args.base_url.rstrip("/") + u
        try:
            r = session.get(url, timeout=10, allow_redirects=True)
        except Exception as e:
            print(f"[!] GET {url} failed: {e}")
            continue

        fname = re.sub(r"[^A-Za-z0-9]", "_", url)
        outpath = save_dir / f"{fname}.txt"
        save_file(outpath, r.content)

        print(f"\n=== {url} ===")
        print(f"Status: {r.status_code}")
        ct = r.headers.get("Content-Type","")
        print(f"Content-Type: {ct}")
        text = r.text
        print("Preview (first 400 chars):")
        print(text[:400].replace("\n", "\\n"))
        res = analyze_text(url, text)
        if res["flags"]:
            print(">>> FLAGS FOUND in cookie-jar mode:")
            for f in res["flags"]:
                print(f)
                found_any.append(("cookiejar", url, f))
        else:
            print("no flags found in this response (cookie-jar mode)")

    # 2) try sending raw Cookie header with encoded value (some servers expect this)
    print("\n[*] Now trying raw Cookie header with URL-encoded value...")
    headers = {"Cookie": f"{cookie_name}={cookie_enc}", "Origin": "http://localhost:3000", "User-Agent": "flag-finder/1.0"}
    for u in URLS:
        url = args.base_url.rstrip("/") + u
        try:
            r = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        except Exception as e:
            print(f"[!] GET {url} failed: {e}")
            continue

        fname = re.sub(r"[^A-Za-z0-9]", "_", url) + "_enc"
        outpath = save_dir / f"{fname}.txt"
        save_file(outpath, r.content)

        print(f"\n=== {url} (raw-encoded-cookie) ===")
        print(f"Status: {r.status_code}")
        ct = r.headers.get("Content-Type","")
        print(f"Content-Type: {ct}")
        text = r.text
        print("Preview (first 400 chars):")
        print(text[:400].replace("\n", "\\n"))
        res = analyze_text(url, text)
        if res["flags"]:
            print(">>> FLAGS FOUND in raw-header mode:")
            for f in res["flags"]:
                print(f)
                found_any.append(("rawheader", url, f))
        else:
            print("no flags found in this response (raw-header mode)")

    # Summarize
    print("\n\n=== Summary ===")
    if found_any:
        for mode, url, flag in found_any:
            print(f"[{mode}] {url} -> {flag}")
    else:
        print("No flags found. Try the following:")
        print(" - 確認: セッションが有効か（ブラウザでページをログイン状態で再確認）")
        print(" - 別の note id を試す（note?id=2,3,...）")
        print(" - ページ内にスクリプトで生成される可能性があるためブラウザで Console -> document.body.innerText を取得して同じ解析を試す")
        print(" - 反転 (reverse) / ROT13 / base64 以外の単純な置換 (Caesar shift 等) を試す")

if __name__ == "__main__":
    main()
