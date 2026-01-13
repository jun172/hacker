# chat_monitor.py

LOG_FILE = "chat_log.txt"

def save_message(username, content):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        if not content.strip():
            f.write(f"{username}: null\n")
        else:
            f.write(f"{username}: {content}\n")

def show_recent_logs(n=5):
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print("=== Recent Logs ===")
        for line in lines[-n:]:
            print(line.strip())

def main():
    print("チャット監視システム開始（終了するには 'exit' と入力）")
    while True:
        username = input("ユーザー名: ")
        content = input("メッセージ: ")

        if content.lower() == "exit":
            print("終了します。")
            break

        save_message(username, content)
        print("保存完了")
        show_recent_logs()

if __name__ == "__main__":
    main()
