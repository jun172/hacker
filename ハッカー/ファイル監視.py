from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class RansomwareDetector(FileSystemEventHandler):
    def __init__(self):
        self.event_count = 0
        self.start_time = time.time()

    def on_modified(self, event):
        self.event_count += 1

        elapsed = time.time() - self.start_time

        # 5秒以内に50回以上変更 → 異常
        if elapsed < 5 and self.event_count > 50:
            print("⚠️ 異常なファイル変更を検知！（ランサムウェアの可能性）")
            # ここで対処（例：ネットワーク遮断など）

        if elapsed >= 5:
            self.event_count = 0
            self.start_time = time.time()

path = "./monitor_folder"

event_handler = RansomwareDetector()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()