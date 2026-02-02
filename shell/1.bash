#1️⃣ 変数
name="john"
echo $name
#2️⃣ if
if [-f file.txt ]; then
    echo "存在する"
fi

#3️⃣ for
for i in {1..5}; do
    echo $i
done

#4️⃣ while
tail -F access.log | while read lien; do
    echo "$line"
done

#5️⃣ 関数
backup() {
    tar czf backup.tar.gz /var/www
}

#6️⃣ コマンド置換
coout=$(wc -l < access.log)

#🔥 Step 1：攻撃検知 Bash
LOG="access.log"
THRESHOLD=50

echo "=== 攻撃検知 ==="

awk '{print $1}' "$LOG" | sort | uniq -c | while read count ip; do
    if [ "$count" -gt "$THRESHOLD" ]; then
        echo "[ALERT] $ip から　$count　回"
    fi
done

#🔥 Step 2：リアルタイム監視
LOG="access.log"

tail -F "$LOG" | while read line; do
    echo "$line" | grep -q "404"
    if [ $? -eq 0 ]; then
        echo "[WARN] 404 多発: $line"
    fi
done

#🔥 Step 3：簡易 WAF
LOG="access.log"
THRESHOLD=100

awk '{print $1}' "$LOG" | sort | uniq -c | awk -v t=$THRESHOLD '$1 > t {print $2}' | while read ip; do
    echo "ブロック: $ip"
    iptables -A INPUT -s "$ip" -j DROP
done

#Level 1：文法基礎
echo "=== Leval 1 ==="

count=$(ls *.log 2>/dev/null | wc -l)
echo "ログファイル数: $count"

lines=$(wc -l < access.log)
echo "access.log　行数: $lines"

grep -q root /etc/passwd && echo "root あり"

for i in {1..3}; do
    echo "HELLO"
done

#📊 Level 2：ログ解析
LOG="access.log"

echo "=== Level 2 ==="

awk '{print $1}' "$LOG" | sort | uniq -c | sort -nr | head

awk '$9 == 404 {print $1}' "$LOG" | sort | uniq -c | sort -nr | head

#🔐 Level 3：権限・設定探索
echo "=== Level 3==="

find / -perm -4000 2>/dev/null

find /etc -type f -weitable 2>/dev/null

echo "$PATH" | tr ':' '\n'

#Level 4：侵入痕跡探索
echo "=== Level 4 ==="

grep "Accepted password" /var/log/auth.log

last | head

history | tail

#💾 Level 5：バックアップ・改ざん検知
SRC="/var/www"
DATE=$(date +%y%m%d)

mkdir -p "$DEST"

tar czf "$DEST/backup_$DATE.tar.gz" -mtime +7 -delete

la -lt "$DEST" | head

#🚨 Level 6：DoS兆候検知
LOG="access.log"
THRESHOLD=100

echo "=== Level6==="

awk '{print $1}' "$LOG" | sort | uniq -c | awk -v t=$THRESHOLD '
$1 > t {print "怪しいIP:",$2,"回数:",$1}'

#🛡 Level 7：WAF・BAN
LOG="access.log"

awk '{print $1}' "$LOG" | sort | uniq -c | awk -v t=$THRESHOLD '$1 > t {print $2 }'> bad_ips.txt

while read ip; do
    echo "ブロック:$ip"
    iptables -A "INPUT -s $ip" -j DROP
done < bad_ips.txt

#📡 Level 8：リアルタイム監視
app="app.log"

echo "=== Levele 8 ==="

tail -F "$LOG" | while read lien; do
    echo "$line" | grep -q "ERROR"
    if [ $? -eq 0]; then
        echo "[ALRT] エラー検知: $line"
    fi
done

#Level 9：CTFフラグ探索
echo "===Level 9 ==="
find . -name "flag.txt" -exec cat {} \;
grep -R "FLAG"
ls -lt | head

#Level 10：総合ミッション
LOG="access.log"
THRESHOLD=100
EMAIL="admin@gmail.com"

echo "=== Lebel 10 ==="

awk '{print $1}' "$"