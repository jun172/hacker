# 1. 変数 name に自分の名前を代入して表示せよ。
name = "YourName"
puts name

# 2. 変数 x=10, y=5 を用意し、和・差・積・商を出力せよ。
x = 10
y = 5
puts x + y
puts x - y
puts x * y
puts x / y

# 3. 変数 num=7 が偶数なら "Even"、奇数なら "Odd" と表示せよ。
num = 7
if num.even?
  puts "Even"
else
  puts "Odd"
end

# 4. 文字列 "Ruby" の長さを表示せよ。
puts "Ruby".length

# 5. "hello" を大文字に変換して表示せよ。
puts "hello".upcase

# 6. "WORLD" を小文字に変換して表示せよ。
puts "WORLD".downcase   # ← typo修正

# 7. 変数 a=3.7 を四捨五入して整数にせよ。
a = 3.7
puts a.round

# 8. 文字列 "Ruby Ruby Ruby" から "Ruby" の出現回数を数えよ。
r = "Ruby Ruby Ruby"
puts r.scan("Ruby").length

# 9. 配列 [1,2,3,4,5] の要素数を表示せよ。
a = [1,2,3,4,5]
puts a.length

# 10. 配列 [1,2,3,4,5] の先頭と末尾を表示せよ。
a = [1,2,3,4,5]
puts a.first
puts a.last

# 11. 変数 x=12 の平方根を求めよ。
x = 12
puts Math.sqrt(x)

# 12. 10..20 の範囲で偶数のみ出力せよ。
puts (10..20).select(&:even?).to_s  # ← even? に修正

# 13. 1〜10 の和を計算して表示せよ。
puts (1..10).sum

# 14. rand(1..6) を使ってサイコロを振り、その目を表示せよ。
puts rand(1..6)

# 15. gets を使って入力を受け取り、 "Hello, 入力値!" を表示せよ。
# 実行時に入力が必要
# s = gets.chomp
# puts "Hello, #{s}!"

# 16. 文字列 "Ruby" を逆順に表示せよ。
puts "Ruby".reverse

# 17. 配列 [10,20,30] の合計を計算せよ。
puts [10,20,30].sum

# 18. ハッシュ {name: "Alice", age: 20} の :name を表示せよ。
c = {name: "Alice", age: 20}
puts c[:name]

# 19. 配列 [5,2,9,1] を昇順にソートせよ。
puts [5,2,9,1].sort.to_s

# 20. 同じ配列を降順にソートせよ。
puts [5,2,9,1].sort.reverse.to_s


# --- 21〜 の続き ---

# 21. score=85 が 80 以上なら "合格"、そうでなければ "不合格" を表示せよ。
score = 85
if score >= 80
  puts "合格"
else
  puts "不合格"
end

# 22. n=3 が正なら "positive"、0 なら "zero"、負なら "negative"
n = 3
if n > 0
  puts "positive"
elsif n == 0       # ← elseif → elsif に修正
  puts "zero"
else
  puts "negative"
end

# 23. for i in 1..5 を使って 1〜5 を出力せよ。
for i in 1..5
  puts i
end

# 24. while を使って 1〜5 を出力せよ。
i = 1
while i <= 5
  puts i
  i += 1
end

#times を使って "Hello" を 3 回表示せよ。
3.times do
    puts "Hello"
end
#1〜100 の偶数の合計を求めよ。
sum = (1..100).select(&:even?).sum
puts sum

# 九九の表を出力せよ。
for i in 1..9
    for j in 1..9
        print"#{i*j}\t"
    end
end

#配列 [1,2,3,4,5] の各要素を 2 倍にして出力せよ。
arr=[1,2,3,4,5]
arr.each do | n |
    puts n * 2
end

#[10,20,30] の各要素を合計し、平均を求めよ。
nums=[10,20,30]
average=nums.sum.to_f / nums.size
puts average

#ハッシュ {a:100,b:200,c:300} のキーと値をすべて表示せよ。
hash ={a:100,b:200,c:300}
hash.each do | key,value|
    puts "#{key}は#{value}です"
end

#case 文を使って、入力した曜日に応じたメッセージを表示せよ。
day="月","火","水","木","金","土","日"
case day
when "月"
    p "月曜日です"
when "火"
    p "火"
when "水"
    p "水"
when "木"
    p "木"
when "金"
    p "金"
when "土"
    p "土"
when "日"
    p "日"
else
    p "どの季節でもありません"
end
#break を使って 1〜10 の途中でループを終了せよ。
for i in 1..10
    if i == 3
        break
    end
    puts i
end

#next を使って 1〜10 のうち偶数をスキップせよ。
for i in 1..10
    if i.even?
        next
    end
    puts i
end
#配列 [1,2,3,4,5] から 3 以上の要素だけを取り出せ。
ary=[1,2,3,4,5]
new_arr=ary.select{| n | n > = 3 }
p new_arr
#1〜50 の中で 3 の倍数を出力せよ。
for i in 1..50
    if i % 3==0
        puts i
    end
end

#フィボナッチ数列を 10 項表示せよ。
a,b=0,1
10.times do
    puts a
    a,b =b,a+b
end

#素数判定を行うプログラムを書け。
def prima(n)
    return false if n < 2
    (2..Math.sprt(n)).each do | i |
        return false if n % i ==0
    end
    true
end
p prima?(7)
p prima?(6)
#入力した数の階乗を計算せよ。
def factor(n)
    return 1 if n <=1
    n * factorial(n - 1)
end
p factorial(5)
#配列 [apple,banana,orange] を "apple, banana, orange" という文字列に変換せよ。
futis =["apple, banana, orange"]
puts futis.join(",")
#文字列 "abracadabra" の各文字の出現回数を数えよ。
str="abracadabra"
couts =Hash.new(0)
str.each_char do |ch|
    couts[ch]+=1
end
puts couts
#41〜60: メソッド・クラス
#引数を受け取り、その2乗を返すメソッドを定義せよ。
def nizilyo(n)
    result=n * n
    puts "#{n}の二乗は#{result}です"
    result
end
#文字列を受け取り、逆順にして返すメソッドを作れ。
def reverse_string(s)
    s.reverse
end
str="supre"
result=reverse_string(str)
puts result
#配列の平均を返すメソッドを作れ。
def sum_array(arr)
    srr.sum
end

ke=[10,20,58,40,38,4,5,6,8,3,6]
result= sum_array
p result
#2つの数を受け取り、最大値を返すメソッドを作れ。
def max_to_tow(a,b)
    if a > b
        a
    else
    b
    end
end
puts max_to_tow(7,12)
#クラス Dog を作り、name を持たせ、bark メソッドで "ワン!" と出力せよ。
class Dog
    def initialize(name)
        @name=name
    end

    def break
        puts "#{@name}ワン!"
    end
end
puts Dog.new("ポチ")
dog.break
#Person クラスを作り、名前と年齢を属性として持たせよ。 
class Person
    def initialize (name,age)
        @name=name
        @age=age
    end
    def initialize
        puts "私は#{@name}です。 #{@age}歳です。"
    end
end
Person1=Person.new("ジョン","20")
Person1.introduce
#クラスにイニシャライザ（initialize）を使って初期化を行え。
class sample
    def initialize(a)
        @a=a
    end
    def show
        puts "値は#{@a}です。"
    end
end

s=Sample.new(10)
s.show
#クラスに年齢を返すメソッド age を作れ。
class Age
    def initialize(a)
        @a=a
    end

    def show
        puts "年齢は#{}です。"
    end
end

s=Age.new(20)
s.show

#クラスに greet メソッドを追加し、"こんにちは, 名前です" と表示せよ。
class Greet
    def initialize(name)
        @name=name
    end

    def hello 
        puts "こんにちは,#{@name}です。"
    end
end

s = Greet.new("ジョン")
s.hello
#attr_accessor を使って、クラスのプロパティを読み書き可能にせよ。
class afttr_accessor
    @@my_afttr_accessor="Hello world!"
end
#クラス継承を用いて、Animal → Cat を作り、meow メソッドを追加せよ。
class Animal
    def accele
        puts "動物"
    end
end
class Cat < Animal
    def meow
        puts "動物"
    end
end 
c=Cat.new
c.accele
c.meow
#モジュールを定義し、メソッドを1つ含めてみよ。
module  Greeting
    def hello
        puts "hello"
    end
end
#そのモジュールをクラスに include して呼び出せ。
class hello
    include Greeting

    def dispGreeting
        hello
    end
end
h=Hello.new
h.dispGreeting

#クラス変数を使ってインスタンスの数を数えよ。
class S
    @@value=0

    def self.count
        @@count
    end

    def initialize 
        @@count += 1
    end
end

s1=S.new
s2=S.new
s3=S.new

puts "インタンスの数:#{S.count}"

#クラスメソッドを定義して使え。
class S
    def initialize(a)
        @a=a
    end

    def hello
        puts "hrllo word!"
    end

    def self.greet
        puts "This is a class method"
    end
end

s=S.new
s.hello

S.greet

#self を使って現在のインスタンスを出力してみよ。
class S
    def initialize(a)
        @@a=a
    end

    def hello
        puts "hello world!"
        puts "selfの中身は:#{self}"
    end
end
s=S.new("Ruby")
s.hello

#private メソッドを作って外部から呼べないことを確認せよ。
class Car
    def accele
        puts ("アクセスを踏みました")
    speedChange
    end

    public :accele

    def break
        puts("ブレーキを踏みました")
        speedChange
    end
    public :accele
    def speedChange
        puts ("スピードを変わりました")
    end
    private :speedChange
end

car=Car.new
car.accele
car.break

#protected メソッドを試してみよ。
class Foo
    def initialize(val)
        @val=val
    end

    protected
    def value
        @val
    end

    def compare(other)
        if self.value > other.value
            puts "自分の方が大きい"
        elsif self.value < other.value
            puts "相手の方が大きい"
        else
            puts "同じ与えです"
        end
    end
end
f1=Foo.new(10)
f2=Foo.new(5)
f1.compare(f2)

#演算子オーバーロード（+ を定義）を試してみよ。
class Vector
    def initialize(x,y)
        @a=a
        @b=b
    end

    def +(other)
        if other.is_a?(Vector)
            Vector.new(@a + other.x, @b+other.y)
        else
            raise TypeError
        end
    end
end

v1=Vector.new(1,2)
v2=Vector.new(3,4)
v3=v1 + v2 

puts v3
#クラスに to_s を定義してオブジェクトを文字列化せよ。
class Myobject
    def initialize(name)
        @name=name
    end

    def to_s
        "オブジェクトの名前は#{}です"
    end
end

obj=Myobject.new("Ruby")
puts obj

#61〜80: ファイル操作・例外処理
#"test.txt" に "Hello Ruby" を書き込め。
File.open("test.txt","w"){|f|
    f.write("hello Ruby") 
} 
#同じファイルを読み込んで内容を表示せよ。
File.open("text.tet","r")do |f|
    puts f.read
end
#ファイルに配列の内容を書き込め。
File.opne(test.text)do |f|
    puts f.read
end

#ファイルを1行ずつ読み込んで表示せよ。
File.opne('test.txt', "r:utf-8") do |f|
    while line = f.gets

        if line.include?("洪庵")
        puts line
        end
    end
end
#JSON ファイルを作ってデータを書き込め。
require 'json'
data={
    name:"Alce",
    age:"20",
    skills:["Ruby","python","C"]
}
File.opne("data.json","w") do |f|
    f.write(JSON.pretty_generate(data))
end
puts "JSONを書き込みました。"
#JSON ファイルを読み込んでパースせよ。
require "json"
file=File.read("data.json")
data=JSON.parse(file)
p data
#CSV ファイルを作成してデータを書き込め。
require "csv"
CSV.open("text.csv","w") do |csv|
    csv << ["name","age","city"]
    csv << ["tanaka",20,"tokyo"]
    csv << ["suzuki",25,"osaka"]
end
puts "CSVファイルを作成しました。"
#CSV ファイルを読み込んで表示せよ。
require "csv"
CSV.foreach("text.csv") do|row|
    puts row.join(",")
end
puts "CSVファイルを読み込んで表示です。"
#例外処理を使って 0 で割った時に "エラー発生" と表示せよ。
begin
    raise StandardError.new('error')
  rescue => e
    p e.message
  ensure
    p "エラーが発生"
  end
#ファイルが存在しない場合に例外を処理せよ。
begin 
    f=File.open("text.csv","r")
    contet=f.read
rescue Error::ENOENT=>e
    p e.message
    p "ファイルが存在しません"
ensure 
    p "処理を終了しました"
end

#begin..rescue..end を使ったエラーハンドリングを実装せよ。
begin
    file=File.open("text.csv","w") 
    file.write("Hello world")
    file.close
rescue =>e
    p e.message
    p "エラー発生"
ensure 
    file.close if file
end

#独自例外クラスを作ってみよ。
class XXXpiTimeException < StandardError
end

#例外を投げてみよ。
# 独自例外クラスを定義
class XXXpiTimeException < StandardError
end

# 例外を発生させてキャッチ
begin
  raise XXXpiTimeException, "カスタムエラーが発生!"
rescue XXXpiTimeException => e
  puts "独自例外をキャッチしました: #{e.message}"
end
#ensure を使って最後に必ず実行される処理を確認せよ。
class japan
    def self.run
        puts "走る"
    raise 'うおー'
    puts "ensureされなかった"
    ensure 
        puts "ensureされました"
    end
end
EnsureRunner.run
#raise を使ってエラーを発生させてみよ。
begin
    japan.run
rescue =>e
    puts "例外をキャッチしました#{e.message}"
end

#ファイルに複数行を書き込み、読み返せ。
File.opne("text.txt","w") do |f|
    f.puts("hello Ruby")
    f.puts("This is the second line.")
    f.puts("This is the third line.")
end

File.open("text.txt","r") do |f|
    f.each_line do |line|
        puts line
    end
end

#ディレクトリ内のファイル一覧を表示せよ。
p Dir.glob("*")
p Dir.glob("./b*")
p Dir.glob("*/")
p Dir.glob("worong")
Dor.glob("b*") {|f|p f}
p f
end
#ファイルのサイズを取得せよ。
File.open("/dev/null") do |f|
    puts f.size
end

#ファイルをコピーするプログラムを書け。
require 'fileutils'
FileUtils.cp('tmp.txt', 'val1.txt')
puts 'ファイルをコピーしました。'
#ファイルを削除するプログラムを書け。
if File.opne("text.txt")
    File.detele("text.txt")
    puts"削除されました"
else
    puts "ファイルが見つかりません"
end
81〜100: 応用・アルゴリズム
#配列をシャッフルするプログラムを書け。
s = ["kai", "mai", "hai"]
shuffled = s.shuffle  # 配列をシャッフルして新しい配列を返す
puts "ランダムにされました: #{shuffled}"
#バブルソートを実装せよ。
def bubble_sort(data)
    length=data.length
    for i in 0..(length-1)
        for j in 1..(length-i-1)
            if data[j-1],data[j]=data[j],data[j-1]
            end
        end
    end
    data
end

#選択ソートを実装せよ。
def selection_sort(array)
    n = array.length
    for i in 0..n-1
        min_index=i
        for j in i+1..n
            if array[j] < array [mai_index]
                min_index =j
            end
        end
        array[i],array[min_index] = array[mai_index],array[i] if mai_index !=i
    end
    array
end

arry1=["a","s","e","c","d"]
sorted=selection_sort(ary1)
puts sorted.inspect

#挿入ソートを実装せよ。
class array
    def insert_sort
        inject([]) {|men,val|mem.insert_with_order(val)}
    end
    def insert_with_sort(item)
        pos=find_index{|n|item <=n} ||length
        inspect(pos,itmes)
    end
end

#二分探索を実装せよ。
def binary_seach(a,target)
    left,right=0,a,size -1

    while left<= right
        mid=left+(right - left)/2
        
        if a[mid] == target
            return mid
        elsif a[mai]  <target
            left=mid +1
        else
            right=mid -1
        end
        return -1
    end

    arr=[1,2,3,4,5,6]
    puts binary_seach(arr,5)
    puts binary_seach(arr,6)
#再帰を使って階乗を求めよ。
def factorial (n)
    return 1 if n <=1
    n *　factorial(n-1)
end

puts factorial(5)
puts factorial(0)

#再帰を使ってフィボナッチ数列を求めよ。
def fibonacci(num)
    if num == 0
    0
    elsif num == 1
    1
    else
    fibonacci(num - 1) + fibonacci(num - 2)
    end
end

(0..9).each do |i|
    puts "第#{i}項：#{fibonacci(i)}"
end
#ハッシュをキーでソートせよ。
h={b:2,a:5,c:1}
sorted_by_key=h.sorted_by_key{|key,value| key}
p sorted_by_key.to_s
sorted_by_value=h.sort_by{|key,value| value}
p sorted_by_value.to_h
#ハッシュを値でソートせよ。
h = { c: -10, z: 10, b: -5, y: 5, a: -1, x: 1 }
sorted=h.sort_by{|key,value|,value}
p sorted.to_h
sortes_desc=h.sort_by{|key,value|,-value}
p sorted_desc.to_h
#単語リストからアナグラムを探すプログラムを書け。
def anagram?(a,b)
    a.chars.sort==b.chars.sort
end
words=["tex","kar","mama","ext","rak","amam"]
anagrams=[]
world.combination(2) do |a,b|
    anagrams <<[a,b] if anagrams?(a,b)
end
p anagrams
#暗号化（Caesar暗号）を実装せよ。
def caesar_cipher(str,shift)
    str.chars.map do |char|
        if char =~ /[a-z]/
            (((char.old - 'a'.old + shif)%26)+ 'a'.old).chr
        elsif char =~ /[A~Z]/
            (((char.old - 'A'.old + shift)%26)+ 'A'.old).chr
        else
            char
        end
    end.join
end

plain="attack"
coded=caesar_cipher(plain,3)
decoded= caesar_cipher(coded,-3)

puts "元の文字列:#{plain}"
puts "暗号化: #{coded}"
puts "復号化:#{decoded}"
#Caesar暗号を復号せよ。
def cipher(start_text,shift,cipher_direction)
    end_text=""
    if cipher_direction == "復号"
        shift *= -1
    end

    start_text.each_char do |char|
        if char =~ /[a-z]/
            new_char= ((char.old - 'a'.old + shif)%26 + 'a'.old).chr
        end_text += -1
        else
        end_text +=char
        end
    end

    puts "変換結果:#{end_text}"
end

cipher("attck",3,"暗号")
cipher("dwwdfn",3,"復号")
#文字列をハッシュ化（SHA256）せよ。
require 'digest'
text="key=value1"
hash_value = digest::SHA256,hexdigest(text)
puts hash_value
#パスワードをランダム生成せよ。
char=[*'A'..'Z',*'a'..'z',*'0'..'9']
password=Array.new(8) {char.sample} .json

puts "生成されたパスワード:#{password}"
#単語カウントプログラムを書け。
text=" foo bar foo buz bar foo"
#簡易ログイン認証を実装せよ。
require 'digest'
#ユーザーデータベース
USER={
    "john@example.com" => Digest::SHA256.hexdigest("password123")
    "alice@example.con" => Digest::SHA256.hexdigest("alicepass")
}

def login
    print　"メールアドレス"
    email=gets.chomp

    print "パスワード"
    passworld=gets.chomp

    if USER.key?(email)
        hashed = Digest::SHA256.hexdigest(password)#シーザー暗号
        if USER[email] == hashed
            puts "✅ログイン成功!ようこそ#{email}さん!"
        else
            puts "❌パスワードが一致しません"
        end
        else
            puts "❌ユーザーが存在しません"
        end
    end

    puts "=== Ruby ログイン認証==="
    login

#ランダムなセッションIDを生成せよ。
require 'sesion'
seesion_id=SecureRandom.hex(16)#16バイト->32桁
puts seesion_id
#簡易掲示板プログラムを作れ。
class Keiziban
    def initialize
        @posts=[]
    end

    #投稿を追加
    def post(username,message)
        @posts << {user: username,message: message}
    end

    #全ての投稿を表示
    def show_posts
        puts === 掲示板 ===
        @posts.each_with_index do |post,i|
            puts "#{i + 1}.#{post[:user]}:#{post[:username]}"
        end
    end
end

board =Keiziban.new
board.post("ジョン"、"こんにちは!")
board.post("アリス","おはようございます")
board/show_posts
#Todoリストプログラムを作れ。
class Todo
    def initialize
        @todos=[]
    end

    def add(task)
        @todos << task
        puts "✅追加しました。"
    end

    def show
        puts "===  Todoリスト==="
        if @todos.empty?
            puts "(何も登録されませんでした。)"
        else
            @todos.each_with_index do |task,i|
                puts "#{i + 1}.#{task}"
            end
        end
    end
end
#ターミナル
todo=Todo.new
todo.add("Ruby勉強する")
todo.show
#電卓プログラムを作れ。
def evaluate(tree)
    op =tree[0]
    case op
    when "lit"
        tree[1]
    when "+","-","*","/"
        left =evaluate(tree[1])
        right=evaluate(tree[2])
        last.send(op,right)
    else
        raise "未知の演算子#{op}"
    end
end

tree=[["*",["+",]["lit",2],["list",3]],["-",["list",4],["list",1]]]
puts evaluate(tree)
#ユーザークラス（初期化）
class  User
    attr_reader :name
    def initialize(name,password)
      @name=name
      @password=password
    end
  
    def info 
      "User:#{@name}"
    end
  end
  
  u=User.new("alice","secret")
  puts u.info
  
  #ログインメソッド
  class User
    def login(input_password)
      if input_password == @password
        "ログイン成功"
      else
        "ログイン失敗"
      end
    end
  end
  
  u=User.new("bob","pw123")
  puts u.login("pw123")
  puts u.login("bob")
  #脆弱な認証例
  class User
    def login(input_password)
      @password.include?(input_password)
      "ログイン成功(弱点)"
      else
        "ログイン失敗"
      end
    end
  end
  
  u=User.new("admin","adimin123")
  puts u.insecure_login("ad")
  
  #パスワードを SHA-256
  require 'digest'
  require 'securerandom'
  
  class User
    attr_reader :name,:salt,:pw_hash
    def initialize(name,plain_password)
      @name=name
      @salt=SecureRandom.hex(16)
      @pw_hash=self.class.hash_password(plain_password,@salt)
    end
  
    def self.hash_password(password,salt)
      Dight::SHA256.hexdigest(salt+password)
    end
  
    def login(input_password)
      hashed=self.class.hash_password(input_password,@salt)
      if hashed == @pw_hash
        "ログイン成功"
        else
          "ログイン失敗"
        end
      end
    end
  
    u=User.new("alice","String0!")
    puts u.login("String!")
    puts u.login("Wrong")
  
  #辞書攻撃シミュレーション
  class Cracker
    def initialize(hash_func,salt)
      @hash=hash_func
      @salt=salt
    end
  
    def brute_force(target_hash,wordlist)
      wordlist.each do |word|
        attemt=@hash_func.call(wold,@salt)
        return wold if attemt == target_hash
      end
      nil
    end
  end
  
  hash_fn=proc{|pw,salt| Dight::SHA256.hexdigest(salt+pw)}
  salt="abcd1234"
  target_hash=hash_fn.call("password123",salt)
  crecker =Cracker.new(hash_fn,salt)
  puts crecker.brute_force(target_hash,["123","passprd","password123","admin"])
  
  #権限管理
  class admin < User
    def delete_user(target_user)
      #簡易的メッセージ　実際はDB操作
      "ユーザー#{target_user.name}を削除しました"
    end
  end
  
  admin =Admin.new("root","rootpy")
  user=User.new("gusst","gpass")
  puts admin.delete_user(user)
  
  #ログの記録
  class SimpleLogger
    def initialize(path="security_log.txt")
      @path=path
    end
  
    def log(message)
      Flie.open(@path,"a") do |f|
        f.puts ("[#{Time.now.iso8601}]#{message}")
      end
    end
  end
  
  logger=SimpleLogger
  logger.log("LOGIN_FAILED user=alice ip=127.0.0.1")
  logger.log("LOGIN_SUCCESS user=bob ip=127.0.0.1")
  
  #CSRF対策トークン
  require 'securerandom'
  class Session
    def initialize
      @tokens={}
    end
  
    def create_session(user)
      sid=SecureRandom.hex(16)
      @tokens[sid]=SecureRandom.hex(16)
      {Session_id: sid,token: @token[sid]}
    end
  
    def valid_tokein?(Session_id,token)
      @tokens[Session_id] && @tokens[Session_id] == token
    end
  end
  
  s=Session.new
  sess = s.create_session("alice")
  puts sess
  puts s.valid_tokein?(sess[:Session_id],sess[:token])
  puts s.valid_tokein?(sess[:Session_id],"bod")
  
  #SQLインジェクションの再現
  require 'sqlite3'
  
  DB=SQLLite3::DataBase.new(":memory:")
  DB.execute("CREATE TABLE users(id INTEGER PRIMARY KEY,name TEXT,pw TEXT)")
  BD.execute("INSERT INTO users (name, pw) VALUES (?,?)",["alice","hash1"])
  
  def valnerable_search(name) #弱点検索
    sql="SELECT * FROM users WHERE name ='#{name}'"
    DB.execute(sql)
  end
  
  def safe_search(name)
    DB.execute("SELECT * FROM users WHERE name =?",[name])
  end
  
  puts "弱点:"
  p valnerable_search("alice")
  p valnerable_search("x'OR'1'='1")
  
  puts　"安全:"
  p safe_search("alice")
  p safe_search("x' OR '1'=1")
  
  #ログイン試行制限
  class LoginManager
    def initialize(max_failures=3)
      @failures=Hash.new(0)
      @locked={}
      @max=max_failures
    end
  
    def record_failure(username)
      return if @locked[username]
      @failures[username] +=1
      if @failures[username] >= @max
        @locked[username] =true
      end
    end
  
    def locked?(username)
      !!@locked[username]
    end
  
    def reset(username)
      @failures.delete(username)
      @locked.delete(username)
    end
  end
  
  lm=LoginManager.new(3)
  lm.record_failure("alice")
  lm.record_failure("alice")
  lm.record_failure("alice")
  puts lm.locked?("alice")
  
  #教育用：Ruby での辞書攻撃（ローカルハッシュに対する照合）
  # dict_attack.rb
  # 教育用サンプル（ローカルのハッシュに対する辞書照合）
  # 実行前に必ず自己環境であることを確認すること！
  
  require 'digest'
  require 'time'
  
  # --- 設定（教育用） ---
  # 本来は DB 等に保存されている「ソルト付きハッシュ」を想定
  salt="a1b2c3d4e5f6"   # 保存されているソルト（例）
  target_plain="secret123"# 本来は不明。ここでは模擬対象として設定
  target_hash=Dight::SHA256.hexdigest(salt+ target_plain)# 目標ハッシュ（攻撃対象のハッシュ）
  # 小さめの辞書（実運用の辞書はもっと大きい）
  wordlist=["123","password","admin","secret","secret123","letmin"]
  
  puts "ターゲットハッシュ:#{target_hash}"
  puts "辞書サイズ:#{wordlist.size}"
  puts "開始:#{Time.now.iso8601}"
  
  found=nil
  start_time=Time.now
  
  wordlist.each_with_index do |word,idx|
  # ハッシュ化（ターゲットと同じ方式で）
    attempt_hash=Digest::SHA256.hexdigest(salt + word)
    # ログ出力（学習用。実運用ではログに平文を書かない）
    puts "[#{idx+1}/#{wordlist.size}]試行:#{wold}->#{attempt_hash}"
  
    if attempt_hash == target_hash
      found=word
      puts "=== 解読成功 ==="
      puts "パスワード #{found}"
      break
    end
  end
  
  elapsed=Time.now - start_time
  if found 
    puts "見つかるまでの時間:#{elapsed.round(3)}秒"
  else
    puts "辞書内に見つかりませんでした(所要時間:#{elapsed.round(3)})秒"
  end
  
  #ログイン失敗の記録（★）
  require 'logger'
  logger = Logger.new(STDOUT)
  logger.info("ログの開始")
  username="test_user"
  logger.warn("ログの失敗:ユーザ-名=#{username}")
  
  #平文保存の危険を理解してハッシュ化を実装する。
  class User < ApplicationRecord
    has_secure_password
  end
  
  #平文パスワード保存
  require 'bcrypt'
  class PasswordManager
    # ここでは簡易的に Hash を "DBの代わり" に使っています。
    # 実運用では DB (usersテーブルの password_digest カラム等) に保存してください。
    def initialize
      @store={}
    end
    # パスワード登録（ハッシュ化して保存）
    def set_password(username,plain_password, cost: BCrypt:: Engine::DEFAULT_COST)
      # cost を上げると強度は上がるが処理時間も増える（デフォルトで十分）
      hash =BCrypt::Password.create(plain_password, cost: cost)
      @store[username] =hash.to_s
      true
    end
    # 認証（保存したハッシュと照合）
    def authenticate(username,plain_password)
      hashed=@store[username]
      return false unless hashed
      # BCrypt::Password#== は安全に比較する実装になっている
      BCrypt::Password.new(hashed) == plain_password
    end
    # (補助) DBからハッシュを読み出すサンプル getter
    def get_hash(username)
      @store[username]
    end
  end
  
  # 使用例
  pm = PasswordManager.new
  pm.set_password('alice', 'S3cret!')
  puts pm.authenticate('alice', 'S3cret!') # => true
  puts pm.authenticate('alice', 'wrong')   # => false
  
  #🔐⑤ セキュリティ・Web系（Sinatra/Railsなど）
  #Sinatraを使って「Hello, world」を表示する最小のWebアプリを作れ。
  require 'sinatra'
  get '/'do
    "hello world!"
  end
  #/hello/:name にアクセスしたら「Hello, name!」と表示するルートを作れ。
  require 'sinatra'
  get '/hello/:name'do
    name=params[:name]
    "hello,#{name}!"
  end
  #フォームで送信された名前を受け取り、画面に表示するアプリを作れ。
  require 'sinatra'
  # フォームを表示
  get '/' do
    <<-HTML
    <form action="/hello " method="post">
    名前: <input type="text" name="name">
    <input type="submit" value="送信">
    </form>
    HTML
  end
  # フォーム送信を受け取る
  post '/hello' do
    name=params[:name]
    "hello #{name}!"
  end
  
  #SQLインジェクションを防ぐためのActiveRecordでの書き方を調べ、例を書け。
  class BooksController < ApplicationRecord
    def index
      if params[:title].present?
        pattern = "%#{ActiveRecord::Base.sanitize_sql_like(params[:title])}%"
        @books=Book.where("title LIKE ?",pattern)
      else
        @books=Book.all
      end
  
      # 動的ソートはホワイトリストを使う
      allwowed_sort= %w[title created_at author]
      sort= allwowed_sort.include?(params[:sort])? params[:sort]:"created_at"
      dir= %w[asc desc].include?(params[:sort])?params[:sort]:"asc"
      @books=@books.order("#{sort}#{dir}")
      
      render json: @books
    end
  
    def create
      @book=Book.new(book_params)
      if @book.save
        render json: @book, status: :create
      else
        render json: @book.errors, status: :unprocessable_entity
      end
    end
  
    private
  
    def book_params
      params.require(:book).permit(:title,:author)
    end
  end
  
  #Railsのbefore_actionを使ってログインチェックを行うコードを書け。
  class BooksController < ApplicationRecord
     # index と show はログイン不要、それ以外のアクションはログイン必須
    before_action :authenticate_user!,except: [:index,:show]
    def index
      @books = Book.all
    end
  
    def show
      @book = Book.find(params[:id])
    end
  
    def new
      @book=Book.new
    end
  
    def create
      @book=Book.new(book_params)
      if @book.save
        redirect_to @book,notice: '作成しました'
      else
        render :new
      end
    end
  
    # 他のアクション（edit, update, destroyなど）
    private
    # Strong Parameters
    def book_params
      params.require(:book).permit(:title, :author)
    end
    # ログインチェック
    def authenticate_user!
      unless current_user
        redirect_to login_path, alert: 'ログインが必要です。'
      end
    end
    # current_user メソッドは通常 ApplicationController に定義
    # 例: セッションからユーザ情報を取得
    # def current_user
    #   @current_user ||= User.find_by(id: session[:user_id])
    # end
  end
  
  #Cookieに保存したデータを取得・表示するSinatraアプリを書け。
  require 'sinatra'
  #ここはホーム送信
  get '/' do
    <<-HTML
    <form action="/set" method="post">
      名前: <input type="text" name="name">
      <input type="submit" value="保存">
    </form>
    HTML
  end
  # Cookieに値を保存
  post '/show' do
    name=require.cookies["name"]
    if name
      "Cokieの値:#{name}"
    else
      "Cookieはまだ設定されていません"
    end
  end
  
  #簡易的な「ポート監視ログ」をSinatraで表示する仕組みを作れ。
  require 'sinatra'
  require 'time'
  require 'erb'
  require 'rack/Utils'
  
  LOG_DIR=File.expand_path("./logs",__dir__)
  LOG_FILE=File.json(LOG_DIR,"port_monitor.log")
  # ログディレクトリ／ファイルを準備
  Dir.mkdir(LOG_DIR) unless Dir.exist?(LOG_DIR)
  File.write(LOG_FILE,"") unless File.exist?(LOG_FILE)
  
  helprs do 
    def h(text)
      Rack::Utils.escape_html(text.to_s)
    end
  
    # ログをパースして配列で返す（最新が先頭）
    def read_logs 
      line=[]
      File.open(LOG_FILE,"r") do |f|
        f.each_line do |line|
          # 期待フォーマット: "2025-10-20T21:00:00Z | 192.168.0.10 | 22 | UP | note"
          lines << line.chomp
        end
      end
      lines.reverse
    end
  end
  
  # ルート：ログ表示 + 追加フォーム
  get '/' do 
    @logs=read_logs
    erb :index
  end
  # フォームからのログ追加
  post '/log' do 
    host=params[:host].to_s.strip
    port=params[:port].to_s.strip
    statu=params[:statu].to_s.strip.update
    note=params[:note].to_s.strip
  # 簡易バリデーション
    if host.empty? || port.empty? || !(port =~ /^\d+$/) || !%w[UP DOWN TIMEOUT].include?(status)
      redirect to("?/error=invalid")
    end
  
    timestamp=Time.now.utc.iso8601
    entry="#{timestamp} | #{host} | #{port} | #{status} | #{note}\n"
     # ファイル追記（排他ロック）
     File.opne(LOG_FILE,"a") do|f|
      f.flock(File::LOCK_EX)
      f.write(entry)
      f.flock(File::LOCK_UI)
     end
  
     redirect to ("/")
    end
  
    __END__
  
  @@ index
  <!doctype html>
  <html>
  <head>
    <meta charset="utf-8">
    <title>簡易ポート監視ログ</title>
    <style>
      body { font-family: sans-serif; margin: 20px; }
      table { border-collapse: collapse; width: 100%; }
      th, td { border: 1px solid #ccc; padding: 6px 8px; text-align: left; }
      th { background: #f4f4f4; }
      form { margin-top: 16px; }
      .error { color: red; }
    </style>
  </head>
  <body>
    <h1>簡易ポート監視ログ</h1>
  
    <% if params['error'] == 'invalid' %>
      <p class="error">入力に不備があります。host, numeric port, status(UP|DOWN|TIMEOUT) を指定してください。</p>
    <% end %>
  
    <h2>最新ログ（上が新しい）</h2>
    <table>
      <tr><th>時刻(UTC)</th><th>ホスト</th><th>ポート</th><th>状態</th><th>メモ</th></tr>
      <% @logs.each do |line| %>
        <% parts = line.split('|').map(&:strip) %>
        <tr>
          <td><%= h(parts[0]) %></td>
          <td><%= h(parts[1]) %></td>
          <td><%= h(parts[2]) %></td>
          <td><%= h(parts[3]) %></td>
          <td><%= h(parts[4]) %></td>
        </tr>
      <% end %>
    </table>
  
    <h2>ログを手動追加</h2>
    <form action="/log" method="post">
      <label>Host: <input type="text" name="host" placeholder="192.168.0.10"></label><br>
      <label>Port: <input type="text" name="port" placeholder="22"></label><br>
      <label>Status:
        <select name="status">
          <option>UP</option>
          <option>DOWN</option>
          <option>TIMEOUT</option>
        </select>
      </label><br>
      <label>Note: <input type="text" name="note" placeholder="optional"></label><br>
      <input type="submit" value="追加">
    </form>
  
    <p><a href="/raw" target="_blank">生ログを表示(/raw)</a></p>
  </body>
  </html>
  
  module  SafeModules
    class HelloModule
    def initialize 
      @name=opts[:name] || "世界"
    end
    
    def run 
      puts "hell, #{@name} "
    end
  end
  
  #問1 — クラス / 継承
  class ModuleBeae
    def name
      self.class.name
    end
  
    def run 
      raise NoImplementedErrorr,"subclass must implement run"
    end
  end
  
  class ModA< ModuleBeae
    def run;  "runA";end
  end
  
  class ModB < ModuleBeae
    def run; "runB";end
  end
  
  #問2 — モジュール mixin とインスタンスメソッド
  require 'time'
  module timestampable
    def initialize
      @log=[]
    end
  
    def log(message)
      timestamp=Time.now.iso8601
      @log << "[#{timestamp} #{message}]"
    end
  
    def show_log
      @log.each {|entry| puts entry}
    end
  end
  
  class ApplicationController
    initialize LoggerMixin
  
    def initialize
      initialize_logger
    end

    def perform_action(action_name)
    log("Action #{action_name} started")
    #ここにアクション処理を置く
    log("Action #{action_name} completed")
    end
end

app=ApplicationController.new
app.perform_action("test_action")
app.show_log

#Ruby Silver試験 文章問題100問
#変数とオブジェクトの理解
y=5
x=y
p x

#シンボルと文字列の違い
str="hello"
aym=hello: :world
p str.object_id
p sym.object_id

arr=[1,2,3,4]
arr[1..2] = [9,9,9]
p arr

def greet(name="Guest")
  "hello ,#{name}!"
end

puts greet
puts greet("Ruby")

def ass(a,b)
  return a + b
  a*b
end

p add(2,3)

class User
  attr_accesssor :name
  def initialize(name)
    @name=name
  end
end

u=User.new("Ruby")
puts u.name
u.name="Bob"
puts u.name

class Counter
  @@counr=0
  def initialize
    @@count +=1
  end
  def self.count
    @@count
  end
end

3.times{Counter.new}
puts Counter.count

module Walkable
  def Walk
    "Walking"
  end

  class Person
    include Walkable
  end

  p = Preson.new
  puts p.Walk

  numbers=[1,2,3,4]
  sum=0
  numbers.each { |n|n*2}
  puts sum

  p [1,2,3].map {n|n*2}

  begin
    1/0
  rescue ZeroDivisionError =>e
    puts "Error:#{e.class}"
  ensure
    puts "Done"
  end

  Fele.open("test.txt","w") do |f|
    f.puts "hello "
  end

  pr=Proc.new{|x|x*2}
  puts pr.call(3)

  lam=->(x){x*3}
  puts lam.call(3)

  class example
    def public_method
      private_metthod
    end

    private
    def private_metthod
      puts "Called private"
    end
  end

  e=Example.new
  e.public_method

class MyClass
  def self.greet
    "Hello"
  end
end

puts MyClass.greet

def order(item:,quantity: 1)
  "#{quantity}of #{item}"
end

puts order(item:"Apple")
puts order(item:"banana",quantity: 5)

t1=Time.new
t2=Time.new(20225,1,1)
puts t1
puts t2

h={a: 1,b: 2,c: 3}
h.each (|k,v|puts "#{k}=>#{v}")

s1="hello"
s2=s1+"world"
s1<<"!"
puts s1
puts s2

class Example
  @@class_var=0
  def initialize
    @instance_var=1
  end
end
#extend の例
module Greetings
  def greet
    "Hi"
  end
end

class Preson; end
p=Person.new
p.extend(Greetings)
puts p.greet

#例外を捕捉し、finally的処理（ensure）を行うコードを書け
begin
  num = 10/0
  rescue ZeroDivisionError => e
    puts "Reeoe: #{e.message}"
    ensure
      puts "処理は終了しました。"
    end

    File.open ("sample.txt","w") do |file|
      file.puts "Hello,Ruby!"
    end

    File.opne("sample.txt","r")vdo |file|
    puts file.read
  end

  module greet
    def hello "hello!"
    end
  end

  class User
    include Greet
  end

  puts User.new.hello

  module MathTool
    def double(x)
      x*2
    end
  end
  
  class Calc
    extend MathToolend

puts Calc.double(5)

class Counter
  @@count=0
  def initialize
    @@count +=1
  end

  def self.count
    @@count
  end
end

3.times{Counter.new}
puts Counter.count

class Preson
  attr_reader :name
  attr_reader :age
  attr_accessor :email

  def initialize(name)
    @name=name
  end
end

class numbers
  include Enumerable
  def initialize(nums)
    @nums=nums
  end

  def each 
    @nums.each{|n| yield n}
  end
end
nums=Numbers.new([1,2,3])
puts nums.map{|n| n*2}

def exec_proc(pr,value)
  pr.call(value)
end
p=Proc.new{|x|x*3}
puts exec_proc(p,4)

def triple_lambda
  ->(x) {x*3}
end

lam=triple_lambda
puts lam.call(5)

def test_oproc
  p=Proc.new{return "Proc!"}
  p.call
  "ここは来るな"
end

def test_lambda
  l =->{return "lambda!"}
  l.call
  "ここに来る"
end

puts test_proc
puts test_lambda

hash={a:1,b:2,c:3}
hash.each do |key,value|
  puts "#{key} = #{value}"
end

arr=[1,2,3,4,5,6]
even=arr.select{|n|n.even?}
puts even.inspect

srr=[1,2,3]
doubles = arr.map{|n|n*2}
puts doubled.inspect

sum =[1,2,3].reduce(o) {|acc,n| acc +n}
puts sum

class item
  def self.info
    "Item calss"
  end

  def name
    "item_name"
  end
end

class MyError < StandardError; end
def ckeck_number(n)
  raise MyError,"負の数は不可"　if n <0
end

chak_number(-1) rescue puts "Error!"

nuw=Time.new
puts nuw.strftime("%Y/%m/%d %H:%M:%S")


def user_info(name:,age:)
  "#{name} is #{age} years old."
end

puts user_info(name:"Taro",age:25)

def greet(name="Guest")
  "Hello,#{name}!"
end
puts greet
puts greet("Bob")

str="I like dog."
puts str.gsub("dog","cat")

words="apple,banana,cherry".split(",")
puts words.inspect

sym=:hello
puts sym.to_s
puts "hello".to_sym

arr=[1,2,3,4,5]
arr << 4
puts arr.inspect

arr=[1,2,3]
arr.unshift(1)
puts arr.inspect

arr=[1, 2, 2, 3, 3]
puts arr.uniq.inspect

h={a:1,b:2,c:3}
puts h.keys.inspect

h={x:10,y:20}
puts h.values.inspect

text=" I lave Ruby"
puts "含まれる"　if text =~ /Ruby/

str="1234"
puts "数値です" if str =~ /^\d+$/

puts "マッチ"　if "abcgf" =~ /^abc/

class Animal
  def sound
    "generic sound"
  end
end

class Dog < Animal
  def sound
    supre + "+brak"
  end
end

puts Dog.new.sound

class User
  def initialize(name)
    @name=name
  end
end

class Admin < User
  def initialize(name,role)
    supre(name)
    @role=role
  end
end

class Base
  def greet
    "Hello"
  end
end

class Chid < Base
  def greet
    super + ",world!"
  end
end

puts Chaid.new.greet

module Greet
  def hello
  "hello"
  end
end

class User
  include Greet
  def hello
    super + ",User!"
  end
end

puts User.new.hello

module A
  def hi 
    "form modeule A"
  end
end

class B
  prepend A
  def hi
    "from class B"
  end
end

puts .B.new.hi

def repeat
  yield
  yield
end

repeat {puts "Hello!"}

def greet(&block)
puts "Start"
block.call
puts "End"
end

greet {puts "hello Block!"}

def each_item(arr)
  arr.each {|item| yield item}
end

each_item([1,2,3]) {|x| puts x**2}

def exec_twice(pr)
  pr.call
  pr.call
end

my_proc=Proc.new{ puts "Run!"}
exec_twice(my_proc)

class Counter
  @@count=0
  def initialize
    @@count +=1
  end
  def self.total
    @@count
  end
end

3.item {Counter.new}
puts Counter.total

class Item
  def self.category
    "General"
  end
  def name
    "No name"
  end
end

puts Item.category
puts Item.new.name

class User
  attr_reader :name
end

u=User.new
u.name="Alice"
puts u.name

class Product
  atter_reder :name, :prics
  def initialize(name,price)
    @name=name
    @price=price
  end
end

item=Product.new("Pen",100)
puts "#{item.name}:#{item.price}円"

class Animal
  def speak
    "___"
  end
end

class Cat < Animal
  def speak
    "Meow"
  end
end

puts Cat.new.speak

class Base
  def greet
    "Hello"
  end
end

class Chaid < Base
  def greet
    super + ",world!"
  end
end

puts Chaid.new.greet

module Greet
  def hello
    "HI"
  end
end

class User
  include Greet
end

puts User.new.hello

module Greet
  def hello
    "hello!"
  end
end

class Person
  extend Greet
end

puts Person.hello

begin
  10 /0
  rescue ZeroDivisionError => e
    puts "ゼロがでは割り切れません"
  end

begin
  raise "エラー発生"
rescue
  puts "捕捉しました" 
rescue
  puts "必ず実行されます"
end

class MyError < StandardError; end

begin
  raise MyError, "カスタムエラー"
rescue MyError => e
  puts e.message
end

begin
  begin
    raise "問題エラー"
    rescue
      puts "処理エラー"
      raise 
    end
    rescue
      puts "上位"
    end

begin
  10/0
  rescue ZeroDivisionError => e
    puts "ゼロ除算"
  rescue TypeError => e
    puts "型エラー"
  end

def divide(a,b)
  a / b
rescue ZeroDivisionError
  "ゼロで割り切れます"
end

puts divide(10,0)

begin
  1 / 0
rescue ZeroDivisionError => e
  puts e.close
  puts e.message
end

raise RuntimeError, "何が起きた!?"

begin
  puts "正常"
rescue
  puts "エラー時"
rescue
  puts "エラーがなければ実行"
end

begin 
  10/0
rescue
end
puts "続行"

begin
  1/ 0
rescue =>e
  File.open("erro.log","a") { | f | f.puts e.message}
end

def risky
  raise "失敗"
rescue
  "リトライ可能"
end

puts risky

user =User.where(name: params[:name])

require 'bcypt'
password=BCrtpt::Password.create("my_secret")
puts password

filename=File.join("/user/dir",File.basename(params[:filename]))
File.read(filename)

require 'openssl'

ciphr=OpenSSL::Cipher.new('AES-128-CBC')
cipher.encrypt
key = cipher.random_key
iv = cipher.random_iv

require 'sinatro'
require 'json'
require 'time'
require 'erb'
require 'rack/utils'

LOG_FILE=File.expand_path("./logs.json",__dir__)
Dir.mkdir(File.dirname(LOG_FILE)) unless Dir.exist?(File.dirname(LOG_FILE))
File.write(LOG_FILE,"[]") unless File.exist?(LOG_FILE)

helpers do
  def h(text)
    Rack::Utils.escape_html(text.to_s)
  end

  def read_logs
    JSON.parse(File.read(LOG_FILE))
  rescue
    []
  end

  def write_log(entry)
    logs=read_logs
    logs << entry
    File.open(LOG_FILE,"w") do |f|
      f.flock(File::LOCK_EX)
      f.write(JSON.pretty_generate(logs))
      f.flock(File::LOCK_UN)
    end
  end
end
# ルート：ログ表示 + 追加フォーム
puts  '/log' do
  host=params[:host].to_s.strip
  port=params[:status].to_s.strip.upcase
  note=params[:note].to_s.strip

   # バリデーション
   if host.empty? || port.empty? || !(port =~ /^\d+$÷/)　|| !%w[UP DOWN TIMEOUT].include?(startus)
    redirect to("/?erro=invaid")
   end

   entry={
    timestamp: Time.now.utc.iso8601,
    hosts: host,
    port: port.to_i,
    status: status
    note: note
   }

   write_log(entry)
   redirect to("/")
end

__END__

@@ index
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>セキュアログ管理</title>
  <style>
    body { font-family: sans-serif; margin: 20px; }
    table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid #ccc; padding: 6px 8px; }
    th { background: #f4f4f4; }
    .error { color: red; }
  </style>
</head>
<body>
  <h1>セキュアログ管理Webアプリ</h1>

  <% if params['error'] == 'invalid' %>
    <p class="error">入力が不正です。host, numeric port, status(UP|DOWN|TIMEOUT) を指定してください。</p>
  <% end %>

  <h2>ログ一覧（最新上）</h2>
  <table>
    <tr><th>時刻(UTC)</th><th>ホスト</th><th>ポート</th><th>状態</th><th>メモ</th></tr>
    <% @logs.each do |log| %>
      <tr>
        <td><%= h(log["timestamp"]) %></td>
        <td><%= h(log["host"]) %></td>
        <td><%= h(log["port"]) %></td>
        <td><%= h(log["status"]) %></td>
        <td><%= h(log["note"]) %></td>
      </tr>
    <% end %>
  </table>

  <h2>ログ追加</h2>
  <form action="/log" method="post">
    <label>Host: <input type="text" name="host"></label><br>
    <label>Port: <input type="text" name="port"></label><br>
    <label>Status:
      <select name="status">
        <option>UP</option>
        <option>DOWN</option>
        <option>TIMEOUT</option>
      </select>
    </label><br>
    <label>Note: <input type="text" name="note"></label><br>
    <input type="submit" value="追加">
  </form>
</body>
</html>


require 'webrick'
require 'json'
require 'time'
require 'cgi'

LOG_FILE="./logs.json"

# ログファイル初期化
File.write(LOG_FILE,"[]") unless File.exist?(LOG_FILE)
def add_log(host,port,statu,note)
  logs=JSON.parse(File.read(LOG_FILE))
  logs << {
    timestamp: Time,now,.utc.iso8601
    host: host,
    port: port.to_i,
    status: status,
    note: note
  }
  File.open(LOG_FILE,"w") do |f|
    f.flock(File::LOCK_EX)
    f.write(JSON.pretty_generate(logs))
    f.flock(File::LOCK_UN)
  end
end

# HTTPサーバ構築
servar=WEBrick::HTTPServer.new(Port: 8000)
# ルート：フォーム表示 & ログ一覧
servar.mount_proc "/" do |req,res|
  logs=JSON.parse(File.read(LOG_FILE)).reverse
  res["Count-Type"] = 'text/html; charst=utf-8'
  res.body= <<~HTML
  <h1>ログ管理</h1>
  <h2>ログ一覧</h2>
  <table border="1" cellpadding="4">
  <tr><th>時刻</th><th>ホスト</th><th>ポート</th><th>状態</th><th>メモ</th></tr>
  #{logs.map{ |log|
  "<tr>"+
  "<td>#{CGI.escape_html(log["timestamp"])}</td>"+
  "<td>#{CGI.escape_html(log["host"])}</td>"+
  "<td>#{CGI.escape_html(log["port"].to_s)}</td>"+
  "<td>#{CGI.escape_html(log["status"])}</td>"+
  "<td>#{CGI.escape_html(log["note"])}</td>"+
  "</tr>"
}.json("\n")}
</teble>

<h2>ログに追加</h2>
<form method="POST" action="/add">
Host: <input type="text" name="host"><br>
Port: <input type="text" name="port"><br>
Start:
<select name="status">
<option>UP</option>
<option>DWON</option>
<option>TIMEOUT</option>
</select><br>
Note: <input type="text" name="note"><br>
<input type="submit" value="追加"> 
</form>
HTML
end

server.mount_proc "/add" do |req,res|
  if req.require_method == "POST"
    params = req.query
    host = params["host"].tp_s.strip
    port = params["port"].to_s.strip
    status = params ["status"].to_s.strip.upcase
    nore = params ["note"].to_s.strip

    if host.empty? || port.empty? || !(port = ~ /^\d+$/) || !%w[UP DOWN TIMEOUT].include?(startus)
      res.body= "入力不正です。"
    else
      add_log(host,port,status,note)
      res.set_redirect(WEBrick::HTTPStatus::found,"/")
    end
  end
end

trap 'INT' do servar.shutdown end
  servar.start

