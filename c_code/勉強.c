//✅ 問1：Hello, World! を出力せよ
#include <stdio.h>
int mian(void){
    printf("hello World");
    return 0;
}

//✅ 問2：自分の名前を出力せよ
#include <stdio.h>
int main (void){
    printf("my name is jyon.\n");
    return 0;
}

//✅ 問3：2つの整数を足して出力せよ
#include <stdio.h>
int main(void){
    int a = 5, b=3; 
    printf("%d\n",a + b);
    return 0;
}

//✅ 問4：改行を2回入れて出力せよ
#include <stdio.h>
int main(void){
    printf("Line1\n\nLine2\n");
    return 0;   
}

//✅ 問5：変数に数値を代入して出力せよ
#include <stdio.h>
int main (void){
    int x =10;
    printf("x =%dn",x);
    return 0;
}

//✅ 問6：小数(float)を出力せよ
#include <stdio.h>
int main(void){
    float pi = 3.14159;
    printf("pi = %.2f\n",pi);
    return 0;
}

//✅ 問7：文字(char)を出力せよ
#include <stdio.h>
int main (void){
    char c ='A';
    printf("Character: %c\n",c);
    return 0;
}
//✅ 問8：定数を宣言して出力せよ
#include <stdio.h>
#define Tax 10
int main (void){
    printf("TAX = %d%%\n",Tax);
    return 0;
}
//✅ 問9：コメントを使って説明を入れよ
#include <stdio.h>
int main (void){
    //ここは何も出力されません
    printf("Commit exaple\n");
    return 0;
}
//✅ 問10：printfで数式を直接出力せよ
#include <stdio.h>
int main (void){
    printf("%d\n",5*3+2);
    return 0;
}
//問11：整数を入力して出力せよ
#include <stab.h>
int main (void){
    int x;
    printf("整数を入力してください:");
    scanf("%d",&x);
    printf("x = %d\n",x);
    return 0;
}
//✅ 問12：2つの整数の和を出力せよ
#include <stdio.h>
int mian(void){
    int a,b;
    scanf("%d %d",&a,&b);
    printf("合計=%d\n",a+b);
    return 0;
}
//✅ 問13：小数を入力して出力せよ
#include <stdio.h>
int main (void){
    float f;
    printf("小数を入力");
    scanf("%f",&f);
    printf("入力値=%.2f\n",f);
    return 0;
}
//✅ 問14：文字を入力して出力せよ
#include <stab.h>
int main (void){
    char c;
    printf("1文字を入力");
    scanf("%c",&c);
    printf("入力文字:%c\n",c);
    return 0;
}
//✅ 問15：整数の2乗を出力せよ
#include <stdio.h>
int main(void){
    int x;
    printf("整数入力:");
    scanf("%d",&x);
    printf("%dの二乗　= %d\n",x,x*x);
    return 0;
}
//✅ 問16：名前を入力して挨拶せよ
#include <stdio.h>
int main(void){
    char name[50];
    printf("あなたの名前を入力:");
    scanf("%s",name);
    printf("Hello, %s!\n",name);
    return 0;
}
//✅ 問17：円の面積を求めよ (r² × 3.14)
#include <stdio.h>
int main(void){
    float r;
    printf("半径を入力:");
    scanf("%f", &r);
    printf("面積= %.2f\n", r*r*3.14);
    return 0;
}
//✅ 問18：3つの整数の平均を出力せよ
#include <stdio.h>
int main(void){
    int a,b,c;
    printf("3つの整数を入力:");
    scanf("%d %d %d",&a, &b,&c );
    printf("平均=%.2f\n",(a + b + c)/3.0);
}
//✅ 問19：年齢を入力して10年後を出力せよ
#include <stdio.h>
int main(void){
    int age;
    printf("年齢を入力");
    scanf("%d",&age);
    printf("10年後は%d歳です。\n",age + 10);
    return 0;
}
//✅ 問20：2つの文字列を連結して出力せよ
#include <stdio.h>
int main(void){
    char s1[50],s2[50];
    printf("二つの単語を入力:");
    scanf("%s %s",s1,s2);
    printf("統合結果: %s%s\n",s1,s2);
    return 0;
}
//問21：入力された整数が正か負かを判定
#include <stdio.h>
int main(void){
    int x;
    printf("整数を入力:");
    scanf("%d",&x);

    if (x>0)
    printf("正の数です。\n");
    else if (x < 0)
    printf("負の数です。\n");
    else 
        printf("0です。\n");

        return 0;
}
//問22：偶数か奇数かを判定
#include <stdio.h>
int main(void){
    int n;
    printf("正数を入力。");
    scanf("%d",&n);

    if (n % 2 == 0)
        printf("ぐうすです。:");
    else 
        printf("奇数です。\n");
    return 0;    
}
//問23：年齢で成人判定（20歳以上）
#include <stdio.h>
int main (void){
    int age;
    printf("年齢の入力:");
    scanf("%d",&age);

    if (age >= 20)
        printf("成人です。");
    else
        printf("未成年です。");

    return 0;
}
//問24：3の倍数かどうか
#include <stdio.h>
int main (void){
    int num;
    printf("整数入力:");
    scanf("%d",&num);

    if (num % 3 == 0)
        printf("3の倍数です。\n");
    else 
        printf("3の倍数ではありません。\n");
    return 0;
}
//問25：点数の評価（80以上で合格）
#include <stdio.h>
int main(void){
    int score;
    printf("点数を入力:");
    scanf("%d",&score);

    if (score >= 80)
        printf("合格!\n");
    else 
        printf("不合格...\n");
    return 0;
}
//問26：最大値を求める（2つの整数）
#include <stdio.h>
int main (void){
    int a,b;
    printf("2つの整数:");
    scanf("%a,%d",&a,&b);

    if (a > b)
        printf("大きさは %d です。 \n",a);
    else if (a < b)
        printf("大きいのは　%d です。\n",b);
    else 
        printf("同じ値");
    return 0;
}
//問27：3つの整数の最大値
#include <stdio.h>
int main (void){
    int a,b,c,max;
    printf("3つの整数を入力");
    scanf("%d %d %d",&a,&b,&c);
    
    max =a;
    if (b > max) max = b;
    if (c > max) max = c;

    printf("最大値は %d です。\n",max);
    return 0;
}
//問28：3つの整数の最小値
#include <stdio.h>
int main (void){
    int a,b,c,min;
    printf("3つの整数を入力:");
    scanf("%d %d %d",&a,&b,&c);
    min=a;
    if (b < min) min = b;
    if (c < min) min = c;
    printf("最小値は %d です。\n",min);
    return 0;
}
//問29：絶対値を求める
#include <stdio.h>
int main (void){
    int x;
    printf("整数を入力:");
    scanf("%d",&x);

    if (x < 0)
        x = -x;
    printf("絶対値 = %d\n",x);
    return 0;
}
//問30：成績評価（90以上A、80以上B、70以上C、それ以下D）
#include <stdio.h>
int main (void){
    int score;
    printf("点数を入力:");
    scanf("%d",&score);

    if (score >= 90)
        printf("評価:A\n");
    else if (score >= 80)
        printf("評価:B\n");
    else if (score >= 70)
        printf("評価:C\n");
    else
        printf("評価:D\n");
    return 0;
}
//問31：閏年の判定
#include <stdio.h>
int main (void){
    int year;
    printf("西暦入力:");
    scanf("%d",&year);

    if ((year & 400 == 0)  || (year % 4 ==0 && year & 100 !=0))
        printf("閏年です。\n");
    else
        printf("閏年ではありません。\n");
    return 0;
}
//問32：点数が0〜100の範囲内か確認
#include <stdio.h>
int mina(void){
    int score;
    printf("整数を入力:");
    scanf("%d",&score);

    if(score > 0 && score < 100)
        printf("範囲内です。\n");
    else 
        printf("範囲外です。\n");
        return 0;
}
//問33：二つの数が等しいかどうか
#include <stdio.h>
int main(void){
    int a,b;
    printf("2つの整数を入力:");
    scanf("%d %d",&a,&b);

    if (a==b)
        printf("等しいです。\n");
    else 
        printf("異なります。\n");
}
//問34：スイッチで曜日を表示（1〜7）
#include <stdio.h>
int main(void){
    int n;
    printf("1~7を入力(1=月,7=日):");
    scanf("%d",&n);

    switch(n){
        case 1: printf("月曜日\n");break;
        case 2: printf("火曜日\n");break;
        case 3: printf("水曜日\n");break;
        case 4: printf("木曜日\n");break;
        case 5: printf("金曜日\n");break;
        case 6:printf("土曜日\n");break;
        case 7:printf("日曜日\n");break;
        default: printf("1~7を入力してください。\n");break;
    }
    return 0;
}
//問35：四則演算をswitchで選択
#include <stdio.h>
int main(void){
    int a,b;
    char op;

    printf("式を入力(例:3+5):");
    scanf("%d %c %d",&a,&op,&b);

    switch (op){
        case '+':printf("%d\n",a + b );break;
        case '-': printf("%d\n",a-b);break;
        case '*':printf("%d\n",a*b);break;
        case '/':
            if (b != 0)printf("%d\n",a /b);
            else printf("0では割り切れません");
            break;
            default:
                printf("不明な演算子です。\n");
        }
        return 0;
}
//問36：季節を判定
#include <stdio.h>
int main(void){
    int month;
    printf("月(1~12)を入力:");
    scanf("%d",&month);

    if (month >= 3 && month < 5)
        printf("春です:\n");
    else if (month >= 6 && month < 8)
        printf("夏です。\n");
    else if (month >= 9 && month < 11)
        printf("秋です。");
    else if (month == 12 || month == 1 || month ==2)
        printf("冬です。\n");
    else
        printf("無効な月です。\n");

        return 0;
}
//問37：成績と出席率で合否判定
#include <stdio.h>
int main(void){
    int score, attendance;
    printf("点数と出席率(%%)を入力:");
    scanf("%d %d",&score,&attendance);

    if (score >= 70 && attendance >= 80)
        printf("合格!\n");
    else 
        printf("不合格です\n");

    return 0;
}
//問38：三角形の成立条件
#include <stdio.h>
int main(void){
    int a,b,c;
    printf("3辺の長さ入力:");
    scanf("%d %d %d",&a,&b,&c);

    if (a + b > c && a + c > b && b + c > a)
        printf("三角形が作れます。\n");
    else 
        printf("三角形は作れません。\n");
    return 0;
}
//問39：点数によるメッセージ（switch）
#include <stdio.h>
int main(void){
    int grade;
    printf("1~5の評価入力:");
    scanf("%d",&grade);

    switch (grade){
        case 5: printf("素晴らしです。\n");break;
        case 4: printf("良いですね。\n");break;
        case 3: printf("普通です。\n");break;
        case 2: printf("努力が必要です。\n");break;
        case 1: printf("もっと頑張りましょう。\n");break;
        default: printf("1~5の範囲で入力してください。\n");
    }
    return 0;
}
//問40：論理演算子の練習（2つの条件）
#include <stdio.h>
int main(void){
    int a,b;
    printf("二つの整数を入力:");
    scanf("%d %d",&a,&b);

    if (a > 0 && b > 0)
        printf("両方の数です。\n");
    else if (a < 0 || b < 0)
        printf("どちらかが負の数です。\n");
    else 
        printf("0が含まれています。\n");
}
//問41：1〜10 を出力せよ
#include <stdio.h>
int main(void){
    for (int i = 1; i <= 10; i++){
        printf("%d",i);
    }
    printf("\n");
    return 0;
}
//問42：1〜n の合計を求めよ
#include <stdio.h>
int main (void){
    int n, sum=0;
    printf ("%d",&n);
    scanf("合計=%d \n",sum);
    return 0;
}
//問43：1〜10 の偶数のみ出力せよ
#include <stdio.h>
int main (void){
    for(int i =1; i <= 10;i++){
        if(i % 2 == 0) printf("%d",i);
    }
    printf("\n");
    return 0;
}
//問44：入力した数の階乗を求めよ
#include <stdio.h>
int main (void){
    int n;
    unsigned long long fact = 1;
    printf ("整数 n を入力");
    scanf("%d",&n);
    if (n < 0) {printf("負の数の階乗は定義しません。\n"); return 0;}
    for (int i = 1; i <= n; i++) fact *= i;
    printf("%d! = %llu\n",n,fact);
    return 0;
}
//問45：1〜9 の九九を出力せよ
#include <stdio.h>
int main(void){
    for (int i = 1;i <= 9; i ++){
        for (int j = 1; j<= 9;j++){
            printf("%2d",i * j);
        }
    printf("\n");
    }
    return 0;
}
//問46：while で 1〜5 を出力せよ
#include <stdio.h>
int mian(void){
    int i = 1;
    while(i<=5){
        printf("%d\n",i);
        i++;
    }
    return 0;
}
//問47：do-while で 1〜5 を出力せよ
#include <stdio.h>
int main(void){
    int i = 1;
    do{
        printf("%d\n",i);
        i++;
    }while (i <= 5);
    return 0;
}
//問48：for で逆順（10→1）を出力せよ
#include <stdio.h>
int main(void){
    for(int i= 10; i>=1; i--) printf("%d",i);
    printf("\n");
    return 0;
}
//問49：for 内で if を使い 3 の倍数をスキップせよ
#include <stdio.h>
int main(void){
    for (int i = 1; i <= 20; i++){
        if(i%3==0) continue;
            printf("%d",i);
    }
    printf("\n");
    return 0;
}
//問50：入力された数までの合計を求めよ
#include <stdio.h>
int main (void){
    int n ,sum =0;
    printf("nを入力:");
    scaf("%d",&n);

    for (int i = 1; i<=n; i++) sum += i;
    printf("合計　= %d\n",sum);
    return 0;
}
//問51：入力値が0ならループを終了せよ
#include <stdio.h>
int main(void){
    int x;
    while (1)
    {
        /* code */
        printf("整数を入力(0を修了):");
        scanf("%d",&x);
        if(x == 0) break;
        printf("入力=%d\n",x);
    }
    return 0;
}
//問52：1〜50 の中で 5 の倍数のみ出力せよ
#include <stdio.h>
int main(void){
    for (int i=1;i<=50; i++){
        if(i % 5==0)printf("%d",i);
    }
    printf("\n");
    return 0;
}
//問53：ネストした for で三角形を描け（'*'）
#include <stdio.h>
int main(void){
    int n = 5;
    for (int i =1; i<=n;i++){
        for(int j=1; j <= i; i++) putchar('*');
        putchar('\n');
    }
    return 0;
}
//問54：九九表を整形して出力せよ（もう一度例）
#include <stdio.h>
int main(void){
    for(int i = 1; i<=9;i++){
        for (int j=1;j <=9;j++)printf("%d",i *j);
        printf("\n");
    }
    return 0;
}
//問55：ユーザーが「exit」と入力するまで繰り返す（文字列ループ）
#include <stdio.h>
#include <string.h>
int main(void){
    char buf[123];
    while (1)
    {
        printf("文字を入力 (exitで終了):");
        if(scanf("%127s",buf) != 1) break;
        if(strcmp(buf,"exit") == 0) break;
        printf("あなたは '%s' と入力しました\n",buf);
    }
    return 0;
}
//問56：1〜100 のうち、3の倍数または5の倍数を出力せよ
#include <stdio.h>
int main(void){
    for (int i =1; i<= 100; i++){
        if(i % 3 == 0|| i % 5 == 0)printf("%d",i);
    }
    printf("\n");
    return 0;
}
//問57：break を使ってループを途中で抜ける例
#include <stdio.h>
int main(void){
    for (int i = 1; i<= 10; i++){
        if(i == 7) break;
        printf("%d",i);
    }
    printf("\n");
    return 0;
}
//問58：continue を使って条件をスキップする例
#include <stdio.h>
int main(void){
    for(int i = 1; i <= 10;i++){
        if(i%2 == 0) continue;
        printf("%d",i);
    }
    printf("\n");
    return 0;
}
//問59：カウンタ変数を2ずつ増やす for 文
#include <stdio.h>
int main(void){
    for(int i = 0; i<=10; i+=2) printf("%d",i);
    printf("\n");
    return 0;
}
//問60：入力した回数分だけ「Hello!」と表示する
#include <stdio.h>
int main(void){
    int n;
    printf("回数を入力:");
    scaf("%d",&n);
    for (int i =0; i < n; i++) printf("hello!\n");
    return 0;
}
//✅ 問61：2つの整数の最大値を返す関数を作りなさい
#include <stdio.h>
int main(int a, int b){
    if(a >b)
        return a;
    else 
        return b;
}

int main(){
    int x,y;
    scanf("%d %d",&x,&y);
    printf("最大値: %d\n",max(x,y));
    return 0;
}
//✅ 問62：配列の合計値を計算する関数
#include <stdio.h>
int main(int a[],int n){
    int total =0;
    for (int i =0;i< n; i++)
        total += a[i];
        return total;
}

int main(){
    int arr[5] = {1,2,3,4,5};
    printf("合計:%d\n",sum(arr,5));
    return 0;
}
//✅ 問63：配列の最大値を返す関数
#include <stdio.h>
int maxArray(int a[],int n){
    int m=a[0];
    for (int i =1;i< n; i++){
        if (a[i] > m)
            m =a[i];
    }
    return 0;
}
int main(){
    int arr[5] = {10,3,25,7,1};
    printf("最大:%d\n",maxArray(arr,5));
    return 0;
}
//✅ 問64：文字列の長さを計算（strlen禁止）
#include <stdio.h>
int mystrlen(char s[]){
    int i = 0;
    while (s[i] != '\0')
    
        /* code */
        i++;
        return i;
    }
    int main(){
        char str[] = "Hello";
        printf("長さ:%d\n",mystrlen(str));
        return 0;
}
//✅ 問65：値渡しと参照渡しの違い（ポインタ演習）
#include <stdio.h>
void swap(int *a,int *b){
    int t = *a;
    *a = *b;
    *b =t;
}
int main(){
    int x =10, y = 20;
    swap(&x,&y);
    printf("x=%d,y=%d\n",x,y);
    return 0;
}
//✅ 問66：再帰関数で階乗を計算
#include <stdio.h>
int fact (int n) {
    if(n == 0)
        return 1;
        return n * fact (n - 1);
}

int main(){
    printf("%d\n",fact(5));
    return 0;
}
//✅ 問67：フィボナッチ数列（再帰）
#include <stdio.h>
int fib(int n){
    if(n <= 1) return n;
    return fib(n-1) + fib(n-2);
}
int main(){
    printf("%d\n",fib(10));
    return 0;
}
//✅ 問68：構造体の定義と利用
#include <stdio.h>

struct Student {
    char name[20];
    int score;
};

int main() {
    struct Student s ={"Taro",80};
    printf("%s の点数: %d\n", s.name,s.score);
    return 0;
}
//✅ 問69：構造体配列＋ループ
#include <stdio.h>
struct Student{
    char name[20];
    int score;
};

int main(){
    struct Student s[3]={
        {"A",70},
        {"B",85},
        {"C",90}
    };
    int total =0;
    for(int i=0;i <3;i++)
        total += s[i].score;
        printf("平均: %d\n",total / 3);
        return 0;
}
//✅ 問70：構造体とポインタ
#include <stdio.h>

struct Point {
    int x;
    int y;
};

int main(){
    struct Point p ={3,5};
    struct Point *pt =&p;

    printf("%d,%d\n",pt->x,pt->y);
    return 0;
}
//✅ 問71：関数ポインタ（超基礎）
#include <stdio.h>

int add(int a, int b) { return a + b; }

int main() {
    int (*fp)(int, int) = add;
    printf("%d\n", fp(3, 4));
    return 0;
}
//✅ 問72：グローバル変数の利用（注意喚起つき）
#include <stdio.h>
int count =0;
void inc() {
    count ++;
}
int main(){
    inc(); inc();inc();
    printf("count = %d\n",count);
    return 0;
}
//✅ 問73：2次元配列の表示
#include <stdio.h>
int main(){
    int a[2][3] = {{1,2,3},{4,5,6}};
    for (int i =0;i <2;i++){
        for (int j=0;j<3;i++)
        printf("%d",a[i][j]);
    printf("\n");
    }
    return 0;
}
//✅ 問74：2つの配列を結合する
#include <stdio.h>
int main(){
    int a[3] ={1,2,3};
    int b[3] = {4,5,6};
    int c[6];

    for (int i =0; i <3;i++) c[i] = a[i];
    for (int i =0; i<3;i++) c[i + 3] = b[i];

    for (int i =0;i<6;i++) printf("%d",c[i]);
    return 0;
}
//✅ 問75：線形探索（検索）
#include <stdio.h>
int search(int a[], int n, int target){
    for (int i = 0; i<n;i++)
        if (a[i] == target) return i;
        return -1;
}
int main(){
    int arr[5] = {3,4,2,9,1};
    printf("位置: %d\n", search(arr,5,9));
    return 0;
}
//✅ 問76：バブルソート
#include <stdio.h>
void bubble(int a[],int n){
    for (int i =0;i<n-1;i++)
        for (int j = 0;j<n-i;j++)
        if (a[j] > a[j + 1]){
            int t = a[j];
            a[j] = a[j+1];
            a[j+1]=t;
        }
}
int main(){
    int arr[5] ={5,1,4,2,3};
    bubble(arr,5);
    for (int i=0; i<5;i++) printf("%d",arr[i]);
    return 0;
}
//✅ 問77：ランダム数配列を作る
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int mian(){
    srand(time(NULL));
    for (int i=0;i<5;i++)
        printf("%d",rand() % 100);
        return 0;
}
//✅ 問78：構造体で座標移動関数
#include <stdio.h>
struct Point{ int x; int y;};
void move(struct Point *p, int dx, int dy){
    p->x += dx;
    p->y += dy;
}
int main(){
    struct Point p={0,0};
    move(&p,3,5);
    printf("%d,%d\n",p.x, p.y);
    return 0;
}
//✅ 問79：選択ソート
#include <stdio.h>
void selection(int a[],int n){
    for (int i=0;i<n-1;i++){
        int min =i;
        for (int j=i+1;j<n;j++);
        int t =a[i];
        a[i] =a[i];
        a[min] = t;
    }
}
int min(){
    int arr[5] = {9,1,4,7,3};
    selection(arr ,5);
    for(int i=0;i<5;i++) printf("%d",arr[i]);
    return 0;
}
//✅ 問80：平均値を返す関数（float使用）
#include <stdio.h>

float average(int a[],int n){
    int total =0;
    for (int i=0;i<n;i++) total += a[i];
    return (float) total / n;
}

int main(){
    int arr[3] = {10,20,30};
    printf("%.2f\n",average(arr,3));
    return 0;
}
// 問81: ファイルに「Hello File!」を書き込む
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE *fp =fopen("log81.txt","w");
    if(!fp){
        printf("ファイルを開けません。\n");
        return 1;
    }
    fprintf(fp,"Hello File!\n");
    fclose(fp);
    printf("log81.txt　に書き込み完了。\n");
    return 0;
}
//問82: ファイルから1行読み込んで表示
#include <stdio.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

int main82(){
    FILE *fp =fopen("log82.txt","r");
    if(!fp){
        printf("ファイルが見つかりません。\n");
        return 1;
    }
    char line[100];
    fgets(line, sizeof(line),fp);
    printf("読み込み内容%s",line);
    fclose(fp);
    return 0;
}
//問83: ファイルに複数行のログを追記する
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

int main83(){
    FILE *fp =fopen("log83.txt","a");
    if(!fp) return 1;

    fprintf(fp,"ログ1:起動しました。\n");
    fprintf(fp,"ログ2:正常に処理しました。\n");

    fclose(fp);
    printf("追記完了。\n");
    return 0;
}
// 問84: 日付付きログを出力する
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int mian84(){
    FILE *fp = fopen("log84.txt","a");
    if (!fp) return 1;
    time_t now = time(NULL);
    struct  tm * tm_info = localtime(&now);

    char time_str[64];
    strftime(time_str,sizeof(time_str),"%Y-%m-%d %H: %M:%S", tm_info);

    fprintf(fp,"[%s] システム起動\n",time_str);
    fclose(fp);
    printf("時刻つきログをほぞんしました。\n");
    return 0;
}
//// 問85: ファイルの中身を1文字ずつ読み取って表示
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int main85(){
    FILE *fp= fopen("log84.txt","r");
    if (!fp){
        printf("ファイルを開く。\n");
        return 1;
    }
    int c;
    while ((c = fgetc(fp)) != EOF){
        putchar(c);
    }
    fclose(fp);
    return 0;
}
//// 問86: ファイルをコピーする

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

int main86(){
    FILE *src = fopen("log84.txt","r");
    FILE *dst = fopen("backup84.txt","w");

    if (!src || !dst){
        printf("ファイル開くことはありません。\n");
        return 1;
    }

    char c;
    while((c =fgetc(src)) !=EOF){
    fputc(c, dst);
    }
    fclose(src);
    fclose(dst);
    printf("ファイルをコピーしました。");
    return 0;
}
// 問87: ファイルの行数を数える
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main87(){
    FILE *fp =fopen("log88.txt","r");
    if(!fp){
        printf("ファイルは開きません。\n");
        return 1;
    }
    int lines = 0;
    char c;
    while ((c = fgetc(fp)) != EOF){
        if(c == '\n')lines ++;
    }
    fclose(fp);
    printf("ファイル行数:%d\n",lines);
    return 0;
}
// 問88: 構造体をファイルにバイナリ保存する
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct Log{
    char message [50];
    int level;
};

int mian88(){
    struct Log log={"システムは稼働中",1};
    FILE *fp =fopen("log_struct.bin","wb");
    if(!fp) return 1;

    fwrite(&log,sizeof(struct Log),1, fp);
    fclose(fp);

    printf("構造体をバイナリ保存します。\n");
    return 0;
}
// 問89: バイナリファイルから構造体を読み取る
#include <stdint.h>
#include <stdarg.h>
#include <string.h>
#include <time.h>

struct Log{
    char message[50];
    int lavel;
};

int main89(){
    struct Log log;
    FILE *fp =fopen("log_struct.txt","rb");
    if(!fp){
        printf("ファイルを見つかりません。\n");
        return 1;
    }
    fread(&log, sizeof(struct Log),1,fp);
    fclose(fp);

    printf("読み込み結果: [%d] %s\n",log.lavel, log.message);
    return 0;
}
// 問90: ログファイル内を検索し、キーワードを含む行を表示
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main90(){
    FILE *fp= fopen("log90.txt","r");
    if(!fp) {
        printf("ファイルが見つかりません。\n");
        return 1;
    }
    char keyword[30];
    printf("検索キーワードを入力");
    scanf("%s",keyword);

    char line[256];
    while (fgets(line, sizeof(line),fp)){
        if (strstr(line,keyword)) {
            printf("ヒット:%s",line);
        }
    }
    fclose(fp);
    return 0;
}
//🔹問91: パスワード入力時に画面に文字を表示せず取得する
#include <stdio.h>
#include <termios.h>
#include <unistd.h>
#include <string.h>

#define MAX_LEN 100

void get_password(char *password, size_t size) {
    struct termios oldt, newt;
    printf("パスワードを入力してください: ");

    // 現在の端末設定を取得
    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;

    // エコーバックをOFF
    newt.c_lflag &= ~ECHO;
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);

    // パスワード入力
    fgets(password, size, stdin);
    password[strcspn(password,"\n")] = '\0';
    // 端末設定を元に戻す
    tcsetattr(STDERR_FILENO, TCSANOW, &oldt);
    printf("\n");
}

int main(){
    char password[MAX_LEN];
    get_password(password,MAX_LEN);
    printf("入力したパスワードの長さ: %lu\n",strlen(password));
    return 0;
}
//🔹問92: パスワード文字列の強度チェック
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int check_strength(const char *password){
    int has_upper = 0, has_lower = 0, has_digit = 0, has_symbol =0;
    int len =strlen(password);

    if (len < 8) return 0;// 8文字未満は弱い

    for(int i =1;i <len ; i++){
        if (isupper(password[i])) has_upper =1;
        else if (islower(password[i])) has_lower =1;
        else if(isdigit(password[i])) has_digit=1;
        else if (ispunct(password[i])) has_symbol = 1;
    }
    int score=has_upper + has_lower + has_digit + has_symbol;
    return score;
}
int main() {
        char pasword[100];
        printf("パスワードを入力:");
        scanf("%99s",pasword);
        int strength = check_strength(pasword);

        switch (strength){
            case 4:printf("強力なパスワード\n");break;
            case 3:printf("中程度なパスワード\n");break;
            case 2:printf("弱いパスワード\n");break;
            default:printf("とても弱いパスワード\n");break;
        }
        return 0;
}
//問93: ファイルSHA256チェックサム生成
#include <stdio.h>
#include <stdlib.h>
#include <openssl/sha.h>

void sha256_file(const char *filename) {
    FILE *file = fopen(filename,"rb");
    if(!file){
        perror("ファイルは開けません。");
        return ;
    }
    unsigned char buffer[4096];
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX ctx;
    SHA256_Init(&ctx);

    size_t bytesRead;
    while ((bytesRead = fread(buffer, 1,sizeof(buffer),file)) !=0)
    {
        SHA256_Update(&ctx,buffer,bytesRead);
    }
    SHA256_Final(hash,&ctx);
    fclose(file);

    printf("SHA256(%s)=",filename);
    for (int i=0;i< SHA256_DIGEST_LENGTH; i++) {
        printf("%02x",hash[i]);
    }
    printf("\n");
}

int main(int argc,char *argv[]){
    if(argc !=2){
        printf("使い方:%s<ファイル名>\n",argv[0]);
        return 1;
    }
    sha256_file(argv[1]);
    return 0;
}
//問94: ファイルの暗号化と復号化（AES-256-CBC）
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/aes.h>
#include <openssl/rand.h>

#define AES_KEYLEN 256
#define AES_BLOCKLEN 16

// ファイルをバイナリで読み込む関数
unsigned char* read_file(const char* filename, long* size) {
    FILE* fp = fopen(filename, "rb");
    if (!fp) {
        perror("ファイルを開けません");
        return NULL;
    }
    fseek(fp, 0, SEEK_END);
    *size = ftell(fp);
    rewind(fp);
    unsigned char* buffer = malloc(*size);
    fread(buffer, 1, *size, fp);
    fclose(fp);
    return buffer;
}

// バイナリをファイルに書き込む関数
void write_file(const char* filename, unsigned char* data, long size) {
    FILE* fp = fopen(filename, "wb");
    fwrite(data, 1, size, fp);
    fclose(fp);
}

// AES暗号化
void encrypt_aes(const unsigned char* in, unsigned char* out, long size, const unsigned char* key, const unsigned char* iv) {
    AES_KEY encryptKey;
    AES_set_encrypt_key(key, AES_KEYLEN, &encryptKey);

    unsigned char iv_copy[AES_BLOCKLEN];
    memcpy(iv_copy, iv, AES_BLOCKLEN);

    for (long i = 0; i < size; i += AES_BLOCKLEN) {
        AES_cbc_encrypt(in + i, out + i, AES_BLOCKLEN, &encryptKey, iv_copy, AES_ENCRYPT);
    }
}

// AES復号化
void decrypt_aes(const unsigned char* in, unsigned char* out, long size, const unsigned char* key, const unsigned char* iv) {
    AES_KEY decryptKey;
    AES_set_decrypt_key(key, AES_KEYLEN, &decryptKey);

    unsigned char iv_copy[AES_BLOCKLEN];
    memcpy(iv_copy, iv, AES_BLOCKLEN);

    for (long i = 0; i < size; i += AES_BLOCKLEN) {
        AES_cbc_encrypt(in + i, out + i, AES_BLOCKLEN, &decryptKey, iv_copy, AES_DECRYPT);
    }
}

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("使い方:\n");
        printf("  暗号化: %s e <入力ファイル> <出力ファイル>\n", argv[0]);
        printf("  復号化: %s d <入力ファイル> <出力ファイル>\n", argv[0]);
        return 1;
    }

    const char *mode = argv[1];
    const char *input = argv[2];
    const char *output = argv[3];

    unsigned char key[32];
    unsigned char iv[AES_BLOCKLEN];

    RAND_bytes(key, sizeof(key));
    RAND_bytes(iv, sizeof(iv));

    long size;
    unsigned char* in_data = read_file(input, &size);

    // パディング（AESは16バイト単位）
    long padded_size = ((size + AES_BLOCKLEN - 1) / AES_BLOCKLEN) * AES_BLOCKLEN;
    unsigned char* padded_in = calloc(1, padded_size);
    memcpy(padded_in, in_data, size);
    unsigned char* out_data = malloc(padded_size);

    if (mode[0] == 'e') {
        encrypt_aes(padded_in, out_data, padded_size, key, iv);
        write_file(output, out_data, padded_size);

        printf("✅ 暗号化完了\n");
        printf("鍵(key): ");
        for (int i = 0; i < 32; i++) printf("%02x", key[i]);
        printf("\nIV : ");
        for (int i = 0; i < AES_BLOCKLEN; i++) printf("%02x", iv[i]);
        printf("\n");
    } else if (mode[0] == 'd') {
        printf("🔐 復号には、元のkeyとIVをコード内に埋め込むか再入力が必要です。\n");
    }

    free(in_data);
    free(padded_in);
    free(out_data);

    return 0;
}
//問95: TCPポートスキャナ（ソケット通信によるポート開放検査）
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <errno.h>

int main(int argc, char *argv[]) {
    if(argv < 4) {
        printf("使い方: %s <IPアドレス> <開始ポート> <終了ポート> \n",argv[0]);
        return 1;
    }

    char *target_ip = argv[1];
    int start_port = atoi(argv[2]);
    int end_port = atoi(argv[3]);

    printf("ターゲット: %s, ポート範囲: %d-%d\n",target_ip,start_port,end_port);

    for(int port = start_port; port <= end_port; port++) {
        int sock = socket(AF_INET,SOCK_STREAM,0);
        if(sock < 0) {
            perror("ソケット作成エラー");
            continue;
        }
        struct sockaddr_in addr;
        addr.sin_family = AF_INET;
        addr.sin_port = htons(port);
        inet_pton(AF_INET,target_ip,&addr.sin_addr);
        // タイムアウト設定（1秒）
        struct timeval tv;
        tv.tv_sec = 1;
        tv.tv_usec = 0;
        setsockopt(sock,SOL_SOCKET,SO_RCVTIMEO,(const char*)&tv,sizeof(tv));
        setsockopt(sock,SOL_SOCKET,SO_SNDTIMEO,(const char*)&tv, sizeof(tv));

        int result = connect (sock,(struct sockaddr*)&addr,sizeof(addr));
        if(result == 0) {
            printf("[OPEN]ポート%d\n",port);
        }
        close(sock);
    }
    printf("スキャン完了\n");
    return 0;
}
//問96：マルチスレッド TCP ポートスキャナ（並列接続で高速化）
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <pthread.h>
#include <errno.h>
#include <sys/time.h>

typedef struct {char ip [64]; int port;} job_t;

void *worker(void *arg){
    job_t *job = (job_t*)arg;
    int sock=socket(AF_INET,SOCK_STREAM,0);
    if(sock < 0) {free(job);return NULL;}
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port=htons(job ->port);
    inet_pton(AF_INET,job->ip,&addr.sin_addr);
    struct timeval tv ={1,0};
    setsockopt(sock,SOL_SOCKET, SO_RCVTIMEO,&tv,sizeof(tv));
    setsockopt(sock,SOL_SOCKET,SO_SNDTIMEO,&tv, sizeof(tv));
    if(connect(sock,(struct sockaddr*)&addr, sizeof(addr)) == 0){
        printf("[OPEN] %d\n", job->port);
    }
    close(sock);
    free(job);
    return NULL;
}

int main(int argc,char *argv[]){
    if(argc <5) {
        fprintf(stderr,"Uasge:%s <IP> <start> <end> <htreads>\n",argv[0]);
        return 1;
    }
    char *ip = argv[1];
    int start = atoi(argv[2]), end= atoi(argv[3]), threads = atoi(argv[4]);
    pthread_t *pool = malloc(sizeof(pthread_t) * threads);
    int t =0;
    for (int port = start; port <= end; port++) {
        job_t *j = malloc(sizeof(job_t));
        strncpy(j->ip, ip,sizeof(j->ip)-1); j->ip[sizeof(j->ip)-1]=0;
        j->port =port ;
        pthread_create(&pool[t],NULL,worker,j);
        t++;
        if (t == threads) {
            for (int i=0;i<t;i++) pthread_join(pool[i],NULL);
            t=0;
        }
    }
    for (int i=0; i<t;i++) pthread_join(pool[i],NULL);
    free(pool);
    printf("Scan finished\n");
    return 0;
}
//問97HTTP HEAD リクエスト
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <netdb.h>

int main(int argc,char *argv[]){
    if(argc!=3) { fprintf(stderr,"Usage: %s <host> <path>\n", argv[0]); return  1;}
    const char *host = argv[1], *path = argv[2];
    struct hostent *he  = gethostbyname(host);
    if(!he) { fprintf(stderr,"gethotbyname failed\n");return 1; }
    int sock = socket(AF_INET, SOCK_STREAM,0);
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(80);
    addr.sin_addr =*(struct in_addr*)he->h_addr;
    if (connect(sock, (struct sokaddr*)&addr, sizeof(addr)) !=0) { perror("connect"); return 1;}
    char req[1024];
    snprintf(req,sizeof(req),"HEAD %s HTTP/1.0\r\nHOST:%s\r\nConnection: close\r\n\r\n",path,host);
    send(sock,req,strlen(req),0);
    char buf[1024];
    int n = recv(sock,buf,sizeof(buf)-1,0);
    if (n <=0) { printf("No response\n"); return 1;}
    buf[n] = 0;
    // ステータス行解析
    char httpver[16]; int code;
    if (sscaf(buf, "%15s %d",httpver, &code)==2) {
        printf("Response: %s %d\n",httpver,code);
    }else{
        printf("Unexpectd response:\n%s\n",buf);
    }
    close(sock);
    return 0;
}
//問98簡易TCPプロキシ（中継＋ログ）
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <sys/socket.h>
#include <sys/select.h>

#define BACKLOG 10
#define BUF_SIZE 4096

int connect_to_target(const char *host, const char *port) {
    struct addrinfo hints,*res,*rp;
    int sfd =-1;
    memset(&hints,0,sizeof(hints));
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    if (getaddrinfo(host, port,&hints,&res) != 0) return -1;
    for (rp =res; rp != NULL; rp = rp-> ai_next) {
        sfd = socket(rp->ai_family, rp->ai_socktype, rp->ai_protocol);
        if(sfd == -1) continue;
        sfd =-1;
    }
    freeaddrinfo (res);
    return sfd;
}
int mian(int argc, char **argv) {
    if (argc != 4){
        fprintf(stderr,"Usage: %s <listen_port> <target_host> <targrt_port>\n", argv[0]);
        return 1;
    }
    const char *listen_port = argv[1];
    const char *target_host = argv[2];
    const char *target_port = argv[3];

    // Create listening socket
    int listen_fd;
    struct addrinfo hints, *res, *rp;
    memset(&hints,0,sizeof(hints));
    hints.ai_family=AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_flags = AI_PASSIVE;
    if (getaddrinfo(NULL, listen_port, &hints, &res) !=0) {
        pettot("getaddrinfo");
        return 1;
    }
    for(rp=res; rp!=NULL; rp=rp->ai_next){
        listen_fd = socket(rp->ai_family,rp->ai_socktype,rp->ai_protocol);
        if(listen_fd == -1) continue;
        int opt =1;
        setsockopt(listen_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
        if (bind(listen_fd, rp->ai_addr , rp->ai_addrlen) == 0 ) break;
        close(listen_fd);
    }
    freeaddrinfo(res);
    if (listen(listen_fd,BACKLOG)== -1) { perror("listen"); return 1;}
    printf("Proxy listening on port %s -> %s:%s\n", listen_port, target_host,target_port);

    while (1)
    {
        struct sockaddr_storage cli_addr;
        socklen_t cli_len= sizeof(cli_addr);
        int client_fd = accept(listen_fd,(struct sockaddr*)&cli_addr, &cli_len);
        if(client_fd == -1) { perror ("accert"); continue;}

        int target_fd = connect_to_target(target_host, target_port);
        if(target_fd== -1) {perror("connct_to_target"); close(client_fd); continue;}

        char buf[BUF_SIZE];
        ssize_t n;
        int maxfd = (client_fd > target_fd ? client_fd : target_fd) + 1;
        fd_set readfds;
        long long c2s_bytes =0, s2c_bytes=0;

        while (1)
        {
            FD_ZERO(&readfds);
            FD_SET(client_fd, &readfds);
            FD_SET(target_fd, &readfds);
            int rv = select(maxfd, &readfds, NULL,NULL,NULL);
            if (rv <0 ) { perror("select"); break; }
            // client -> server
            if (FD_ISSET(client_fd,&readfds)) {
                n = recv(client_fd, buf,BUF_SIZE, 0);
                if (n <= 0) break;
                ssize_t sent = send(target_fd,buf,BUF_SIZE,0);
                if(sent <= 0) break;
                c2s_bytes += sent;
            }
            // server -> client
            if(FD_ISSET(client_fd, &readfds)) {
                n = (target_fd, buf,BUF_SIZE, 90);
                if (n <= 0) break;
                ssize_t sent = send(client_fd , buf, n,0);
                if (sent <=0) break;
                s2c_bytes += sent;
        }     
    }
    // Log summary and close
    printf("Connection closed: c2s=%lld bytes, s2c=%lld bytes\n",c2s_bytes, s2c_bytes);
    close(client_fd);
    close(target_fd);
    }
    close(listen_fd);
    return 0;
}
//問99libpcapでのパケットキャプチャ（pcapファイル保存）
#include <pcap.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <arpa/inet.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>

pcap_dumper_t *dumper =NULL;

void packet_handler(u_char *user, const struct pcap_pkthdr *h, const u_char *bytes) {
    // dump to file
    if (dumper) pcap_dump((u_char*) dumper,h, bytes);

    // simple parse for IPv4 + TCP
    const struct ip*ip_hdr;
    const struct tcphdr *tcp_hdr;
    int eth_hdr_len=14;
    if(h->caplen < eth_hdr_len + sizeof(struct ip)) {
        printf("short packet\n"); return ;
    }
    ip_hdr = (struct ip*)(bytes + eth_hdr_len);
    char src[INET_ADDRSTRLEN],dst[INET_ADDRSTRLEN];
    inet_ntop(AF_INET,&(ip_hdr->ip_src),src, sizeof(src));
    inet_ntop(AF_INET, &(ip_hdr-> ip_dst),dst,sizeof(dst));
    printf("%ld.%06ld len=%u %s proto=%d\n",h->ts.tv_sec,(long)h->len, src,dst, ip_hdr-> ip_p);
}
int main(int argc, char **argv) {
    if (argc !=4) { fprintf(stderr,"Usage: %s <interfase> <out.pcap> <count>\n",argv[0]); return 1; }
    char *iface =argv[1];
    char *outfile = argv[2];
    int cpunt = atoi(argv[3]);

    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_t *handle = pcap_open_live(iface,65535,1,1000,errbuf);
    if (!handle) { fprintf(stderr, "pcap_open_live failed: %s\n"); pcap_close(handle); return 1;}

    dumper =pcap_dump_open(handle,outfile);
    if (!dumper) { fprintf(stderr,"pcap_dump_open failed\n"); pcap_close(handle); return 1;}

    printf("Capturing on %s -> %s (count =%d)\n",iface,outfile, count);
    pcap_loop(handle,count, packet_handler,NULL);

    pcap_dump_close(dumper);
    pcap_close(handle);
    printf("Capture finished\n");
    return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <openssl/sha.h>
#include <pcap.h>

// 1. ポートチェック関数
int check_port(const char *host, int port) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) return 0;

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    inet_pton(AF_INET, host, &addr.sin_addr);

    int result = connect(sock, (struct sockaddr*)&addr, sizeof(addr));
    close(sock);
    return (result == 0);
}

// 2. SHA-256 計算関数
void hash_file(const char *path) {
    FILE *f = fopen(path, "rb");
    if (!f) { perror("fopen"); return; }

    unsigned char buf[4096], hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX ctx;
    SHA256_Init(&ctx);

    size_t n;
    while ((n = fread(buf, 1, sizeof(buf), f)) > 0)
        SHA256_Update(&ctx, buf, n);

    SHA256_Final(hash, &ctx);
    fclose(f);

    printf("SHA256(%s) = ", path);
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++)
        printf("%02x", hash[i]);
    printf("\n");
}

// ★ コールバック関数（Cではこう書く）
void packet_handler(u_char *user, const struct pcap_pkthdr *h, const u_char *bytes) {
    (void)user;  // 未使用警告回避
    (void)bytes;
    printf("Packet captured: length = %u bytes\n", h->len);
}

// 3. パケットキャプチャ
void capture_packets(const char *iface, int count) {
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_t *handle = pcap_open_live(iface, 65535, 1, 1000, errbuf);
    if (!handle) {
        fprintf(stderr, "pcap_open_live failed: %s\n", errbuf);
        return;
    }

    printf("Capturing %d packets on interface %s...\n", count, iface);
    pcap_loop(handle, count, packet_handler, NULL);
    pcap_close(handle);
}

// 4. メイン関数
int main() {
    printf("問100: 総合セキュリティツール\n");

    // ポートチェック
    const char *host = "127.0.0.1";
    int port = 22;
    printf("Port %d on %s is %s\n", port, host, check_port(host, port) ? "OPEN" : "CLOSED");

    // ファイルハッシュ
    hash_file("test.txt");

    // パケットキャプチャ（ループバックの場合: lo または lo0）
    capture_packets("lo", 5);

    return 0;
}

//1. 変数と型目的: int, char などの型を理解する
#include <stdio.h>
int main(){
    int age =25;
    char initial = 'A';
    printf("Age=%d, INnitial=%C\n",age,initial);
    return 0;
}
//2. 配列とポインタ
#include <stdio.h>
int main(){
    int arr[3] ={1,2,3};
    int *p = arr;
    printf("%d %d\n",arr[1],*(p+1));
    return 0;
}
//3. 関数
#include <stdio.h>
int add(int a,int b){ return a+b;}
int main() { printf("%d\n",add(3,4)); return 0;}
//4. ポインタの基本
#include <stdio.h>
int main(){
    int x = 10;
    int *p =&x;
    printf("%d %p\n",*p,p);
    return 0;
}
//5. malloc/free
#include <stdio.h>
#include <stdlib.h>

int main(){
    int *p = malloc(sizeof(int) *3);
    p[0]=10; p[1] = 20; p[2] = 30;
    for(int i=0;i<3;i++) printf("%d\n",p[i]);
    free(p);
    return 0;
}
//6. 構造体
#include <stdio.h>
struct Person { char name[10];int age; };
int main(){
    struct Person p1 = {"Alice",25};
    printf("%s %d\n",p1.name,p1.age);
    return 0;
}
//7. typedef
#include <stdio.h>
typedef struct { char name[10]; int age ;}Person;
int main(){ Person p={"Bob",30}; printf("%s %d\n",p.name,p.age);}
//8. for/while/do-while
for(int i = 0;i<3;i++) printf("%d\n",i);
int j=0;while(i<3) { printf ("%d\n",j); j++;}
//9. 関数ポインタ
#include <stdio.h>
int add(int a,int b){return a+b;}
int main(){ int (*fp)(int ,int )=add; printf("%d\n",fp(3,4));}
//10. ヘッダファイル
#include <stdio.h>
#include "myheader.h"
//11. static
#include <stdio.h>
void f(){ static int c=0; printf("%d\n",c);}
int main(){ f();f();f();}
//12. const
#include <stdio.h>
int main() { const int x=10; printf("%d\n",x);return 0;}
//13. enum
#include <stdio.h>
enum Color{RED,GREEN,BULE};
int main(){ enum Color c=GREEN; printf("%d\n";c);}
//14. union
#include <stdio.h>
union Data{ int i; char c;};
int main() { union Data d; d.i=65; printf("%d %c\n",d.i,d.c);}
//15. 配列を関数に渡す
#include <stdio.h>
void pintArr(int *arr,int n) 
{ 
    for (i=0;i<n;i++) 
    printf("%d ",arr[i]);
}
int main() { 
    int a[3]={1,2,3};
    pintArr(a,3);
}
//16. 再帰関数
#include <stdio.h>
int fact(int n) { return n<= 1?1:n*fact(n-1);}
int main(){ printf("%d\n",fact(5));}
//17. if/switch
#include <stdio.h>
int mian(){ int x=2; swich(x){ case 1:printf("1");break; default; printf("other");}}
//18. ビット演算
#include <stdio.h>
int main(){ int a=5,b=3; printf("%d\n",a&b);}
//19. メモリレイアウト
stack: 関数内変数
heap: malloc
data: global/static
//20. segmentation fault
int *p=NULL; *p=10;
//✅ 第21問：GPIO を ON/OFF してみる（LED 点灯）
#define LED_PIN 13
void setup(){
    pinMode(LED_PIN, OUTPUT);
}

void loop(){
    digitalWrite(LED_PIN, HIGH);
    delay(1000)
    digitalWrite(LED_PIN, OUT);
    delay(1000)
}
//✅ 第22問：ボタン入力を読み取る（GPIO 入力）
#define BUTTON 4
void loop() {
    int start = digitalWrite(BUTTON);
    if (start == HIGH)
        printf("押された");
}
//✅ 第23問：PWMでLEDを明るさ調整
analogWrite(LED_PIN, 128);
//✅ 第24問：タイマー割り込みの基礎
void timer_interrupt(){
    total_led()
}
//✅ 第25問：UARTで文字を送信（シリアル通信）
Serial.begin(9600);
Serial.println("hello UART");
//✅ 第26問：UART で受信してコマンド処理
if (Serial.availlable()){
    char c = Serial.read();
    if (c == '1') digitalWrite(LED_PIN, HIGH);
}
//✅ 第27問：I2C デバイスから値を読む
Wire.beginTransminsion(addr);
Wire.write(reg);
Wire.requestFrom(addr, 1);
int val = Wire.read();
//✅ 第28問：SPI デバイスとの通信
digitalWrite(CS,Low);
digitalWrite(0x55);
digitalWrite(CS, HIGH);
//✅ 第29問：温度センサの値を読み取る
#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/i2c.h"
#include "hardware/adc.h"

// ===== AHT21アドレス =====
#define AHT21_ADDR 0x38

// ===== OLED SSD1306アドレス =====
#define SSD1306_ADDR 0x3C

// ---------- AHT21 読み取り関数 ----------
void read_aht21(float *temperature, float *humidity) {
    uint8_t cmd = 0xAC; // 取得開始コマンド
    uint8_t data[6];

    // AHT21 に計測指示
    i2c_write_blocking(i2c0, AHT21_ADDR, &cmd, 1, false);
    sleep_ms(80);

    // 測定データ取得
    i2c_read_blocking(i2c0, AHT21_ADDR, data, 6, false);

    uint32_t raw_hum = ((data[1] << 12) | (data[2] << 4) | (data[3] >> 4));
    uint32_t raw_temp = (((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]);

    *humidity = (raw_hum * 100.0) / 1048576.0;
    *temperature = ((raw_temp * 200.0) / 1048576.0) - 50;
}

// ---------- SSD1306 の初期化（最小構成） ----------
void ssd1306_init() {
    uint8_t init_cmds[] = {
        0xAE, // display off
        0xA6  // normal display
    };
    i2c_write_blocking(i2c0, SSD1306_ADDR, init_cmds, sizeof(init_cmds), false);
}

// ---------- SSD1306 に文字を送る（超簡易版） ----------
void oled_print(const char *text) {
    uint8_t buffer[32];
    int len = snprintf((char*)buffer, sizeof(buffer), "%s", text);
    i2c_write_blocking(i2c0, SSD1306_ADDR, buffer, len, false);
}

// ---------- メイン ----------
int main() {
    stdio_init_all();

    // I2C 初期化
    i2c_init(i2c0, 100000);  
    gpio_set_function(4, GPIO_FUNC_I2C); // SDA
    gpio_set_function(5, GPIO_FUNC_I2C); // SCL
    gpio_pull_up(4);
    gpio_pull_up(5);

    // ADC 初期化
    adc_init();
    adc_gpio_init(26); // ADC0 = GPIO26
    adc_select_input(0);

    // OLED 初期化
    ssd1306_init();

    while (1) {
        float temp, hum;
        read_aht21(&temp, &hum);

        uint16_t raw = adc_read();
        float brightness = raw / 4095.0f;

        char line[64];
        snprintf(line, sizeof(line),
            "TEMP: %.1f C\nHUM: %.1f %%\nBRT: %.3f",
            temp, hum, brightness);

        oled_print(line);

        sleep_ms(1000);
    }
}

//✅ 第30問：ADC を使って電圧測定
int val=analogRead(A0);
float voltage = val * 3.3 /1023;
//✅ 第31問：モーターをPWMで制御する
analogWrite(MOTOR_PIN, 200)
//✅ 第32問：サーボモータ角度制御
servo.write(90);
//ロボット・IoT の基本センサ。
#include <stdio.h>
#include "pico/stdlib.h"

#define TRIG_PIN 2
#define ECHO_PIN 3

int main() {
    stdio_init_all();

    gpio_init(TRIG_PIN);
    gpio_set_dir(TRIG_PIN, GPIO_OUT);

    gpio_init(ECHO_PIN);
    gpio_set_dir(ECHO_PIN, GPIO_IN);

    while (1) {
        //トリガーパルス
        gpio_put(TRIG_PIN,0);
        sleep_us(2);
        gpio_put(TRIG_PIN, 1);
        sleep_us(10);
        gpio_put(TRIG_PIN, 0);

        //ECHO HIGH待ち
        while (gpio_get(ECHO_PIN) == 0);
        absolute_time_t start = get_absolute_time();

        //ECHO Low待ち
        while (gpio_get(ECHO_PIN) ==1 );
        absolute_time_t end = get_absolute_time();

        //経過時間
        int64_t pulse_time = 
            absolute_time_diff_us(start,end);

        //距離計算
        float distance_cm = pulse_time / 58.0f;

        printf("Distance: %.2f cm/n", distance_cm);

        sleep_ms(1000);
    }
}
//✅ 第34問：LCD 表示（I2C）
lcd.printf("Hello");
//✅ 第35問：組込み用ミニシステム（LED + ボタン + UART）総合問題
#define LED_PIN 9   // PWM が使えるピン
#define LED_PIN 4  // ボタン入力ピン
void setup() {
    pinMode(LED_PIN, OUTPUT);
    pinMode(BUTTON, INPUT_PULLUP);//プルアップ付き
    Serial.begin(9600);
}
void loop(){
    int state = digitalReed(BUTTON);

    if(start == LOW){
        Serial.println("ボタンが押されました。");
    }else{
        analogWrite(LED_PIN,50)
    }
    delay(100);
}
//✅ 第36問：構造体で顧客情報を扱う
#include <stdio.h>

struct Customer {
    int id;
    char name[50];
    int age ;
};

int main() {
    struct Customer c = {1, "tanaka",30};
    printf("ID=%d 名前=%s 年齢=%d\n",c.id, c.name, c.age);
}
//✅ 37問：配列で顧客を複数管理
struct Customer Customers[3] = {
    {1,"A",20},
    {2,"B",30},
    {3,"C",40}
};
for (int i = 0; i < 3; i++){
    printf("%d: %s\n", Customers[i].id, Customers[i].name);
}
//✅ 38問：ファイルにデータを保存（書き込み）
FILE *fp = fopen("data.txt","w");
fprintf(fp, "ID=1 Name=Tanaka\n");
fclose(fp);
//✅ 39問：ファイルから読み込み
FILE *fp = fopen("data.txt", "r");
char buf[100];
fgets(buf, sizeof(buf), fp);
printf("%s\n", buf);
fclose(fp);
//✅ 40問：構造体をファイルに保存（CSV形式)
fprintf(fp, "%d,%s,%d\n", c.id, c.name, c.age);
//✅ 41問：CSVを読み込んで構造体に格納
int id, age;
char name[50];
fscanf(fp,"%d,%[^,],%d",id,name,&age);
//✅ 42問：メニューを持つ基幹システムの基本画面を作る
printf("1.　顧客\n");
printf("2.顧客一覧\n");
printf("3.終了\n");

int choice;
scanf("%d",&choice);
//✅ 43問：顧客を追加登録できる処理
#include <stdio.h>
struct Customer{
    int id;
    char name[50];
    int age;
};

int main(){
    struct Customer c1;

    //入力
    printf("IDを入手");
    scaf("%d",&c1.name);

    printf("名前を入力:");
    scaf("%s", &c1.age);

    printf("年齢を入力");
    scaf("%d", &c1.age);

    FILE *fp = fopen("data.txt","a");
    if(fp = NULL) {
        printf("ファイルオープン失敗\n");
        return 1;
    }

    fprintf(fp, "%d,%s,%d\n",c1.id,c1.name, c1.age);
    fclose(fp);

    printf("保存しました。");

    return 0;
}
//✅ 44問：検索機能（IDで顧客を探す）
for (int i = 0; i < count; i++) {
    if(customers[i].id == target)
        printf("見つけた: %s\n",customers[i].name)
}
//✅ 45問：削除処理（IDで削除）
#include <stdio.h>
#include <string.h>

struct Customer {
    int id,
    char name[50]:
    int age;
};
int main(){
    struct Customer list[100]={
        {1,"Tanaka",20},
        {2,"Suziki",22},
        {3,"Sato",25}
    };
    int count =3;

    int target;
    printf("削除したいIDを入力:");
    scaf("%d",&target);

    int found=0;

    for (int i = 0; i< count; i++) {
        if (list[i].id == target) {
            found= 1;
            printf("削除対象を発見: %s\n", list[i].name);

            //削除後ろの要素
            for (int j = i;j<count - 1; j++){
                list[j] = list[j+1];
            }
            count--;
            break;
        }
    }
    if (!found) {
        printf("該当IDは見つかりました\n");
    }
    //結果表示
    printf("\n削除後の一覧");
    for (int i = 0; i < count; i++){
        printf("%d %s %d\n", list[i].id, list[i].name, list[i].age);
    }
    return 0;
}
//✅ 46問：社員管理システム風に改修（構造体入れ替え）
struct Employee {
    int id,
    char name[50];
    int salary,
};
//✅ 47問：ログファイルへ操作記録を書く
fprintf(log, "AddCustomer id=%d user=admin\n", id);
//✅ 48問：日付・時刻をログに追加
time_t = t = time(NULL);
fprintf(log,"%s: 登録処理\n", ctime(&t));
//✅ 49問：エラー処理の基礎（NULLチェック）
FILE *fp = fopen("data.txt","r");
if(!fp){
    printf("ファイルがありません\n");
    return 1;
}
//✅ 50問：基幹システムミニプロジェクト
#include <stdio.h>
#include <string.h>

#define MAX 100 

struct Customer {
    int id;
    char name[50];
    int age;
};
struct Customer Customers[MAX];
int count =0;

//ログ出力
void writelog(count char *msg) {
    FILE *log = fopen("log.txt","a");
    fprintf(log, "%s\n", msg);
    fclose(log);
}
//CSV保存
void saveCSV() {
    FILE *fp = fopen("customers.csv","w");
    for (int i = 0; i < count; i++) {
        fprintf(fp, "%d,%s,%d\n", customers[i].id, customers[i].name,customers[i].age);
    }
    fclose(fp);
    writeLog("CSV 保存されました。");
}
//顧客登録
void AddCustomer(){
    printf("ID:");
    scaf("%d", &customers[count].id);
    printf("名前:");
    scanf("%d",&Customers[count].age);

    printf("登録完了!\n");
    writeLog("顧客登録されました。");
    count++;
}
// 一覧表示
void listCustomers() {
    printf("---顧客一覧---\n");
    for (int i =0; i <count;i++) {
        printf("%d:%s (%d)\n",customers[i].id,customers[i].name,customers[i].age);
    }
    writeLog("顧客一覧を表示しました。");
}
//--顧客検索(ID)
void searchCustomer(){
    int target;
    printf("検索するID:");
    scanf("%d",&target);
    for (int i = 0; i< count; i++) {
        if(customers[i].id == target){
            printf("見つかりしました->%d %s(%d)\n",
                    customers[i].id, customers[i].name,customers[i].age);
            writeLog("顧客検索しました。");
            return ;
        }
    }
    printf("該当IDの顧客は存在しません。")
}

//---削除(ID指定)
void deleteCustomer(){
    int target;
    printf("削除する ID:");
    sscaf("%d",&target);

    for (int i = 0; i<count;i ++){
        printf("削除しました：%s\n",customers[i].name);
        writeLog("顧客を削除しました。");

        //後ろのデータを詰める
        for (int j = i; j < count - 1; j++) {
            count--;
            return ;
        }
    }
    printf("該当IDは見つかりません。\n");
}
//メニュー
void menu() {
    int choice;

    while (1) {
        printf("\n====基幹システム=====\n");
        printf("1. 顧客登録\n");
        printf("2.顧客一覧\n");
        printf("3.顧客検索\n");
        printf("4.顧客削除\n");
        printf("5.CSV保存"\n);
        printf("0.終了\n");
        printf("================"\n);
        printf("番号を選択\n");
        scanf("%d",&choice);

        switch (choice){
            case 1: AddCustomer(); break;
            case 2: listCustomers(); break;
            case 3: searchCustomer(); break;
            case 4: deleteCustomer(); break;
            case 5: saveCSV(); break;
            case 0: writeLog("シズテム終了"); return;
            default: printf("無効な番号です\n");
        }
    }
}

int main() {
    writeLog("システムを起動");
    menu();
    return 0;
}
//◆ 51問：線形探索の実装（linear_search）
int linear_search(int arr[], int n, int target) {
    for (int i = 0; i< n; i++){
        if (arr[i] == target)
            return i;
    }
    return -1;
}
//◆ 52問：バブルソート
void bubble_sort(int arr[],int n) {
    for (int i = 0; i< n-1;i++) {
        for (int j = 0; j < n - i; j++) {
            if(arr[j] > arr[j+1]) {
                int tmp = arr[j];
                arr[i] = arr[j+1];
                arr[j+1] =tmp;
            }
        }
    }
}
//◆ 53問：構造体配列を age 昇順にソート
struct Person {
    char name[50];
    int age;
};

void sort_person(struct Person arr[], int n) {
    for (int i = 0; i< n < - 1; i++){
        for (int j = 0; j < n - 1- j; j++) {
            if (arr[j].age > arr[j+1].age){
                struct Person tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp
            }
        }
    }
}
//54問：二分探索（binary_search）
int binary_search(int arr[], int n,int target) {
    int left - 0, right = n - 1;

    while (left <= right) {
        int mid = (left + right)/2;

        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}
//55問：再帰による階乗
int factorial(int n) {
    if (n <= 1) return 1;
    return n * fdactorial(n -1);
}
//56問：フィボナッチ（再帰）
int fib(int n) {
    if (n <= 1) return n;
    returnn fib (n -1) + fib(n - 2);
}
//57問：ポインタによる swap
void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
//58問：malloc を使った配列確保 + 合計
int main(){
    int n,
    printf("個数:");
    scaf("%d",&n);

    int *arr = malloc(sizeof(int) * n)

    for (itn i = 0; i < n; i ++) {
        scaf("%d",&arr[i]);
    }

    int sum= 0;
    for (int i = 0; i < n; i++) sum += arr[i];

    printf("合計 = &d\n",sum);

    free(arr);
}
//59問：動的確保した文字列にコピー
char* str_copy(const char *s) {
    char *p = malloc(strlen(s) + 1);
    strcpy(p,s);
    return p;
}
//60問：構造体の動的配列
struct Book {
    int id;
    char title[50];
};

int main() {
    int n;
    scaf("%d",&n);

    struct Book *Books = malloc(sizeof(struct Book) * n);

    for(int i = 0; i < n; i++) {
        scaf("%d %s", &books[i].id, books[i].title);
    }

    for (int i = 0; i < n; i++) {
        printf("%d %s\n",books[i].id, books[i].title);
    }

    free(books);
}
//61問：ファイル行数カウント
int count_lines(const char *filename) {
    FILE *fp = fopen(filename, "r");
    if (!fp) return -1;

    int lines = 0;
    char buf[256];

    while (fgets(buf, sizeof(buf), fp)) {
        lines++;
    }

    fclose(fp);
    return lines;
}
//62問：CSV 1行読み込み
struct Person {
    int id;
    char name[50];
    int age;
};

void read_csv(struct Person *p, const char *line) {
    sscaf(libn, "%d,%[^,],%d", &p->id,p-> name,&p->age);
}
//63問：入力・計算・出力を関数分割
void input(int *a, int *b, int *c) {
    scanf("%d %d %d", a,b,c);
}
int cale(int a, int b, int c) {
    return a + b + c;
}

void output(int sum) {
    printf("合計 = %d\n",sum);
}
//64問：math_utils.h / math_utils.c  math_utils.h
int add(int a, int b);
int sub(int a,int b);
int mul(int a, int b);
int divi(int a, int b);
#include "math_utils.h"

int add(int a, itn b) { return a + b;}
int sub(int a, int b) {return a - b;}
int mul(int a, int b) { return a * b ;}
int divi(int a, int b) { return a　/ b;}
//65問：ログ出力関数
void writeLog(const char *msg) {
    FILE *fp = fopen("log.txt", "a");
    fprintf(fp, "%s\n",msg);
    fclose(fp);
}
//66問：free を正しく使う
int main() {
    int *p = malloc(sizeof(int) * 10);
    free(p);
}
//67問：QuickSort
void quickSort(int arr[], int left, int right) {
    int l = left, r= right;
    int pivot = arr[(left + right) / 2];

    while(l <= r) {
        while (arr[l] < pivot) l++;
        while (arr[r] > pivot) r--;

        if (l <= r) {
            int tmp = arr[l];
            arr[l] = arr[r];
            arr[r] = tmp;
            l++;
            r--;
        }
    }
    if (left < r) quickSort(arr, left,r);
    if ( l < right) quickSort(arr, l, right)
}
//68問：簡易ハッシュ関数
int hash (const char *s) {
    int sum = 0;
    while (*s) sum += *s++;
    return sum;
}
//69問：3ファイル構成（customer モジュール）
struct Customer {
    int id;
    char name[50];
};

void AddCustomer(struct Customer*, int*)
void listCustomers(struct Customer* int*)
void searchCustomer(struct Customer*,int. int);

#include <stdio.h>
#include "costomer.h"

void AddCustomer(struct Customer *c, int *count) {
    scanf("%d %s", &c[*count].id, c[*count].name);
    (*count)++;
}

void listCustomers(struct Customer *C, int n) {
    for (int i - 0; i < n;i++)
    printf("%d %s\n",c[i].name);
}
void searchCustomer(struct Customer *C, int n,int target) {
    for (int i = 0; i< n; i ++)
        if(c[i].id == target)
        printf("Found: %s\n", c[i].name);
}
//70問：ミニアプリ（アルゴリズム統合）
int main(){
    int n;
    printf("要素数:");
    scaf("%d",&n);

    int *arr = malloc(sizeof(int) * n);

    for (int i = 0; i < n; i++)
        scaf("%d",&arr[i]);

        bubble_sort(arr,n);

        int target;
        printf("検索値:");

        int idx = binary_search(arr,n,target);

        if (idx >=0)
            printf("見つかった:%d番目\n",idx);
        else
            printf("見つからない\n");

        writeLog("検索実行");

        free(arr);
}
//第7章：セキュリティ × C言語
#include <stdio.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <time.h>

int check_port_safe(const char *ip, int port ) {
    int sock;
    struct sockaddr_in add;

    sock = socket(AF_INET,SOCK_STREAM, 0);
    if (sock < 0) return -1;

    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    inet_pton(AF_INET, ip, &addr.sin_addr);

    struct timeval tv = {2,0};
    setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(tv));

    int result =connect(sock, (struct sockaddr *) & addr, sizeof(addr));
    close(sock);

    sleep(1);

    return result == 0;
}
int main() {
    if (check_port_safe("127.0.0.1",22))
        printf("Port OPEN\n");
    else
        printf("Port CLOSED\n")
}
//接続ログ記録（IDS 基礎）
#include <stdio.h>
#include <time.h>

void log_connection(const char *ip, int port, const char *status) {
    FILE *fp= fopen("conn.log","a");
    time_t now = time(NULL);

    fprintf(fp, "%s %s:%d %s\n",
            ctime(&now), ip,port,status);
        fclose(fp);
}
int main() {
    log_connection("127.0.0.1",22,"FAILED")
}
//簡易 IDS：失敗回数しきい値検知
#include <stdio.h>

int main() {
    int fail_count = 0;

    while(1) {
        int result;
        printf("接続結果 (0=成功,1=失敗):")
        scaf("%d",&result);

        if (result == 1)
            fail_count++;
        else
            fail_count = 0;

        if (fail_count >= 5) {
            printf("⚠ IDS ALERT:　連続失敗検知\n")
            break;
        }
    }
}
//安全な入力処理（バッファオーバーフロー対策）
#include <stdio.h>

int main() {
    char buf[32];

    printf("入力:");
    fgetc(buf, sizeof(buf),stdin);

    printf("入力内容: %s\n",buf)
}
//ログ改ざん検知（簡易ハッシュ）
#include <stdio.h>

unsigned int simple_hash(const char *s) {
    unsigned int h = 0;
    while (*s) h = h * 31 + *s++;
    return h;
}

int main() {
    char log[] = "LOGIN FAILED";
    printf("HASH=%u\n", simple_hash(log));
}
//同時接続制限（DoS耐性設計）
#define MAX_CONN 5

int current_conn = 0;

void on_connect() {
    if (current_conn >= MAX_CONN) {
        printf("接続拒否 (制限超過) \n");
        return ;
    }
    current_conn++;
}

void on_connect() {
    if (current_conn > 0)
        current_conn--;
}
//バッファオーバーフロー（最頻出）
#include <stdio.h>

int main() {
    char buf[16];
    printf("Input:");
    scaf("%s",buf);
    printf("You said: %s\n",buf);
}
//フォーマットストリング
#include <stdio.h>

int main() {
    char msg[128];
    fgets(msg,sizeof(msg),stdin);
    printf(msg);
}
//Use After Free（UAF）
#include <stdio.h>
#include <stdib.h>

int main() {
    char *p = malloc(16);
    strcpy(p,"CTF");
    free(p);
    printf("%s\n",p);
}
//整数オーバーフロー
#include <stdio.h>

int main() {
    unsigned int size;
    scaf("%u",&size);

    char buf[size];
    gets(buf);
}
//関数ポインタ上書き
#include <stdio.h>

void win(){
    printf("FLAG{dummy_flag}\n");
}

void lose(){
    printf("Try harder\n");
}
int main() {
    void (*fp)()=lose;
    char buf[32];

    scaf("%s",buf)
    fp();
}
