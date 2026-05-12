import argparse

def show_menu():
    print("""
==============================
コマンド受付システム
==============================
[1] scan
[2] attack
[3] status
[4] exit
==============================
""")
    
def main():
    parser = argparse.ArgumentParser(description="コマンド受付システム")
    parser.add_argument("command", nargs="?", help="実行するコマンド")
    args = parser.parse_args()
    
    if args.command:
        cmd = args.command
    else:
        show_menu()
        cmd =  int(input("番号 or コマンド名を入力してしてください:"))
        
        
    if cmd == "1":
        cmd = "scan"
    elif cmd =="2":
        cmd = "attack"
    elif cmd == "3":
        cmd = "status"
    elif cmd == "4":
        sys.exit()
        
    if cmd == "scan":
        print("🔍 scan コマンドが押されました")
    elif cmd == "attack":
        print("💥 attack コマンドが押されました")
    elif cmd == "status":
        print("📊 status コマンドが押されました")
    else:
        print("❌ 不明なコマンド")

if __name__ ==  "__main__":
    import sys
    main()