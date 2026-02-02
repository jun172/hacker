#Challenge 1：フラグを探せ
find . -name "flag.txt"
cat ./path/to/flag.txt

#Challenge 2：怪しいログ行
grep "FLAG" app.log

#Challenge 3：最終更新されたファイル
ls -lt | head -n 2

#Level 2：ログ解析CTF
#Challenge 4：攻撃IPを特定
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -n 1
#Challenge 5：404多発ユーザー
awk '$9 == 404 {print $1}' access.log | sort | uniq -c | sort -nr | head
#Challenge 6：今日の侵入ログ
grep "$(date +%Y-%m-%d)" auth.log | grep "Failed password"

#🕵️ Level 3：権限・設定ミス探索
find / -perm -4000 2>/dev/null

#Challenge 8：書き込み可能な設定ファイル
find /etc -type f -writable 2>/dev/null

#Challenge 9：怪しいPATH
echo $PATH | tr ':' '\n'

#Challenge 10：開いているポート
ss -tuln

#Challenge 11：怪しい外部通信
netstat -tump 2>/dev/null

#Challenge 12：DNS改ざん検査
cat /etc/resolv.conf

#Level 5：バックアップ改ざん
#Challenge 13：消されたバックアップ
find /backup -type f

#Challenge 14：直近の圧縮ファイル
ls -lt *.tar.gz | head

#🛡️ Level 6：マルウェア疑似検査
#Challenge 15：不審プロセス
ps aux | grep -v root

#Challenge 16：自動起動スクリプト
ls /etc/init.d
crontab -l

#Challenge 17：不審通信スクリプト
grep -R "curl" /usr/local/bin

#Challenge 18：sudo実行権限
sudo -l

#Challenge 19：実行可能ファイル
find / -type f -executable 2>/dev/null

#Challenge 20：.bashrc改ざん
grep -i "alias" ~/.bashrc

#Challenge 21：侵入経路推測
grep "Accepted password" auth.log

#Challenge 22：侵入後の痕跡
last
history

#Challenge 23：バックドア探索
find / -name "*backdoor*" 2>/dev/null

#Challenge 24：怪しい通信先
ss -tumap

#疑似DoSトラフィック検知（ログ監視）
LOG="access.log"

awk '{print $1}' "$LOG" | sort | uniq -c | awk '$1 > 100 {print "怪しいIP:",$2,"回数", $1}'

#② SYN Floodっぽい挙動検知
ss -ant state syn-recv | wc -l

#単一IPからの接続数監視
netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq | -c | sort -nr | head

#DoS耐性テスト（ローカル限定・合法）
for i in {1..50}; do
    curl -s http://localhost:8080 > /dev/null &
done
wait
echo "擬似負荷テスト完了"

#⑤ iptablesでDoS防御（Linux）
# 1IPからの同時接続制限
iptables -A INPUT -p tcp --dport 80 -m connlimit --connlimit-above 20 -j DROP
# 1IPの秒間接続数制限
iptables -A INPUT -p tcp --dport 80 -m limit --limit 10/second -j ACCERT

#⑥ Fail2ban風Shell（簡易版）
LOG="access.log"
THRESHOLD=100

awk '{print $1}' "$LOG" | sort | uniq -c | awk -v t=$THRESHOLD '$1 > t {print $2}' > bad_ips.txt

while read ip; do
    echo "ブロック対象: $ip"
done < bad_ips.txt

#Challenge: 疑似DoS犯人IPを特定せよ
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head

#バックアップ自動化
tar czf backup_$(date +%Y%m%d).tar.gz /var/www

#ログローテーション
mv app.log app.log.$(date +%H%M)
touch app.log

#cron自動実行
0 2 * * * /home/user/backup.sh

#攻撃IP特定
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head

#失敗ログ抽出
grep "Failed password" auth.log

#侵入時刻推定
last | head

#ポート確認
ss -tuln

#疎通チェック
ping -c 1 google.com

#DNS調査
nslookup example.com

#SUID探索
find / -perm -4000 2>/dev/null

#書き込み可能ファイル
find / -writable 2>/dev/null

#怪しいプロセス
ps aux

#環境構築
apt install nginx mysql php

#Docker制御
docker ps
docker stop $(docker ps -q)

#バッチ処理
for f in *.txt; do
    wc -l "$f"
done

#ブルートフォース検知
grep "Failed password" auth.log | wc -l

#権限昇格チェック
sudo -l

#① 攻撃検知ツール（ブルートフォース / DoS兆候
LOG="access.log"
THRESHOLD=100

echo "===攻撃検知==="

awk '{print $1}' "$LOG" | sort | uniq -c | sort -nr | while read count ip; do
    if [ "$count" -gt "$THRESHOLD"]; then
        echo "[ALERT] $ip から $count回アクセス"
    fi
done

#② ログ監視ツール（リアルタイム）
LOG="app.log"

echo "===　ログ監視開始  ==="

tail -F "$LOG" | while read line; do
    echo "$(date): $line"
    echo "$line" | grep -q "ERROR" &6 echo "[!]エラー検知"
done

#簡易WAF（怪しいリクエスト遮断）
LOG="acces.log"
BLOCKLIST="block_ips.txt"
THRESHOLD=50

awk '{print $1}' "$LOG" | sort | uniq -c | awk -v t=$THRESHOLD '$1 > t {print $2}' > "$BLOCKLIST"

while read ip; do
    echo "ブロック: $ip"
    iptables -A INPUT -s "$ip" -j DROP
done < "$BLOCKLIST"

#バックアップ自動化ツール
src="/var/www"
DEST="/backip"
DATE=$(date +%Y%m%d)

mkdir -p "$DEST"

tar czf "$DEST/backup_$DATE.tar.gz" "$SRC" && echo "バックアップ成功"

find "$DEST" -name "backup_*.tar.gz" -mtime +7 -delete

#Mission 1
log="access.log"
THRESHOLD=10

echo "=== 攻撃検知==="

awk '{print $1}' "$log" | sort | uniq -c | while read count ip; do
    if [ "$count" -gt "$THRESHOLD"]; then
        echo "[ALERT] 攻撃の疑い: $ipから$count 回アクセス"
    fi
done

#基本版：ERROR検知 → メール送信
LOG="app.oog"
ALERT_WORD="error"
EMAIL="admin@example.com"

tail -F "$LOG" | while read line; do
    echo "$line" | grep -q "$ALERT_WORD"
    if [ $? -eq 0 ]; then
        echo "[$(date)] エラー検知: $line" | mail -s "[ALERT] ログエラー検知" "$EMAIL"
    fi
done

#セキュリティ向け応用  ① 不正ログイン検知 → メール
LOG="/ver/log/auth.log"
EMAIL="admin@example.com"

tail -F "$LOG" | while read line; do
    echo "$line" | grep -q "Failed password"
    if [ $? -eq 0 ]; then
        echo "[$(date)] 不正ログイン: $line" | mail -s "[ALERT] SSHブルフォース" "$EMAIL"
    fi
done

#② DoS兆候 → メール
LOG="access.log"
THRESHOLD=50
EMAIL="adimin@example.com"

awk '{print $1}' "$LOG" | sort | uniq -c | while read count ip; do
    if [ "$count" -gt "$THRESHOLD" ];then
        echo "[$(date)] Dos疑い: $ip から $count　回" \
        | mail -s "[ALERT] Dos兆候検知" "$EMAIL"
    fi
done

#Mission：ログ監視アラートを完成させろ
LOG="app.log"
EMAIL="asimain@example.com"

tail -F "$LOG" | while read line; do
    if echo "$line" | grep -q "HACK";then
        echo "???"
    fi
done

#ab（Apache Bench）
ab -n 1000 -c 50 http://127.0.0.1:8080/

#方法③：siege（本格）
siege -c50 -r20 http://127.0.0.1:8080

#access.logからアクセス回数が一番多いIP
LOG="access.log"
THRESHOLD=100

echo "=== アクセス回数が一番多いIP ==="

top_ip=$(awk '{print $1}' "$LOG" \
    | sort \
    | uniq -c \
    | sort -ne \
    | hesd -n 1)

count=$(echo "$top_ip" | awk '{print $1}' )
ip=$(echo "$top_ip" | awk '{print $2}' )

echo "TOP IP: $ip ($count reqests )"

if [ "$count" -ge "$THRESHOLD" ]; then
    echo "⚠️ 攻撃疑い (しきい値 $THRESHOLD 超え)"
fi

#error.log から 同じエラーメッセージの出現回数を 多い順に表示せよ。
LOG="error.log"

echo "=== エラーメッセージ出現回数 ==="

awk '{$1=""; $2=""; print substr($0,3)}' "$LOG"\
    | sort \
    | uniq \
    | sort -nr

#