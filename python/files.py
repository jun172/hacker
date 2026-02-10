import os

FILES_DIR = "/Users/junnakai/python/python/files"

if not os.path.exists(FILES_DIR):
    print("❌ パスが存在しません")
    exit()

if not os.path.isdir(FILES_DIR):
    print("❌ フォルダではありません")
    exit()

for file in os.listdir(FILES_DIR):
    print("発見:", file)
