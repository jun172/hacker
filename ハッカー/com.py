import argparse

# パーサーを作る
parser = argparse.ArgumentParser(description="argparseのサンプル")

# 引数を定義
parser.add_argument("-n", "--number", type=int, help="数字を入力")
parser.add_argument("-m", "--message", help="メッセージを入力")

# コマンドライン引数を解析
args = parser.parse_args()

print("あなたの入力:")
print("number =", args.number)
print("message =", args.message)
