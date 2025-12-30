import { profile } from "node:console";

let x: number = 10;

let onther: string ="Json";

let isAdmin: boolean = false;

let number: number[] = [1,2,3];

let a: string [] = ["A","B"];
let b: Array<string> = ["C","D"];

let value: string | null | undefined;

value = "hello";
value = null;
value = undefined;

let data: any;
data = 123;
data = "text";
data = true;
data.foo.bar.baz();

let the: unknown;
the = 10;
the = "hello";
the = true;

let other: any;
let  u: unknown;
other.toUpperCase();
u.toUpperCase();

if (typeof u === "string") {
    u.toUpperCase();
}

function throwError(message: string):never{
    throw new Error(message);
}

function asserNever(x: never): never{
    throw new Error("Unex@ected value:" + x);
}

type Role = "admin" | "user";

function checkRole(role: Role) {
    if (role === "admin") return;
    if (role === "user") return;
    asserNever(role);
}

let age: number =30;

let y = 10;
let s = "hello";

let input;
input = "abc";
input =123;

function add(a:number,b:number):number{
    return a + b;
}

let United;
United.foo();

let State = 10;
const is = 10;

let one  = "John";

let of = 123;

let countries; // 初期化なし → any型
let w = JSON.parse("{}"); // any型推論

let highest: number =10;
highest =20;

function healthcare(a: number,b:number): number{
    return a +b;
}

function greet(name:string):void{
    console.log(`Hello,${name}`);
}

function costs(name?:string) {
    if(name){
        console.log(`Hello,${name}`);
    }else{
        console.log("hello");
    }
}
costs();
costs("Taro");

function world(name:string = "Guest"){
    console.log(`Hello,${name}`);
}
world();
world("Taro");

let In:(a: number,b:number) => number;
In= (x,y) => x +y;
console.log(In(2,3));

function greetUser(name:string,callback: (msg:string) =>void) {
    callback(`Hello,${name}`);
}
greetUser("Taro",message => console.log(message));

const multiply:(x:number, y:number) => number=(a,b)=> a*b;
console.log(multiply(2,4));

function sum(...nums:number[]):number{
    return nums.reduce((total,n)=>total+n,0);
}
console.log(sum(1,2,3,4));

function combine(a:string,b:string):string;
function combine(a:number,b:number):number;
function combine(a:any,b:any):any{
    return a +b;
}

console.log(combine(1,2));
console.log(combine("A","B"));

function fail(msg:string):never{
    throw new Error(msg);
}

function infinteLoop(): never{
    while(true){}
}

let person: {name: string; age:number} = {
    name:"taro",
    age:20
};

let car:{ breand:string ; yaer:number} ={
    breand:"Toyota",
    yaer:2026
};

let user:{name:string; age?:number}={
    name:"Hanalo"
};
user.age=25;

let config:{ readonly apiKey:string} = {
    apiKey:"12345"
};


let States: {
    name: string;
    age?: number;
    address: {
      city: string;
      zip: string;
    };
  } = {
    name: "Taro",
    address: {
      city: "Tokyo",
      zip: "123-157"
    }
  };  

  console.log(user.address.city);

let only:{ name: string;age :number } ={
    name:"Taro",
    age:"20"//nuber型にはstirngは代入できない
};

let scores:{ [key: string]: number} = {
    math:80,
    english:90
};
scores["science"] = 70;

let work: { name:string; age?:number} = { name: "Taro"};
if (work.age !== undefined) {
    console.log(work.age + 10);
}

let obj = { a:1,b:2};

let jsObj = { a:1};
jsObj.a = "hello";//JSではOK

let tsObj:{ a:number} = {a:1};
tsObj.a ="hello";//TSではダメ型

interface player {
    name:string;
    hp: number;
    mp:number;
}

interface Enemy extends player {
    attack: number;
}

type GameState ="TITLE" | "PLAYING" | "GAMEOVER";

type challenge = "hp" | "mp" | "atk";

const challenge: Record<challenge,number>={
    hp:100,
    mp:50,
    atk:20
};

interface SaveData {
    hp: number;
    mp: number;
    level: number;
}

const save: Partial<SaveData> ={
    hp:80
};

interface config {
    volume: 50
};

type playerName = Pick<player,"name">;

type playerWithoutMP = Omit<player,"mp">;

interface Charecter {
    name: string;
    hp: number;
    position: {x: number; y: number};
}

type Action = "ATTACk" | "HEAL";

function act (char: Charecter, action: Action) {
    if (action === "ATTACk") {
        char.hp -= 10;
    }
}

function identity<T>(value:T):T {
    return value;
}

identity<number>(100);
identity<string>("hello");

function first<T>(arr: T[]):T {
    return arr[0];
}
first([1,2,3]);
first(["a","b"]);

function pair<T,U>(a: T, b:U) {
    return { a,b };
}

pair("HP",100);

function getLength<T extends { length: number }>(value: T): number {
    return value.length;
}
getLength("hello");
getLength([1, 2, 3]);  

function getValue<T,K extends keyof T>(obj: T,key:K) {
    return obj[key];
}

const player = { name: "Taro",hp:100};
getValue(player,"hp");

interface Item<T> {
    name: string;
    value: T;
}
const potion: Item<number> = {
    name:"HP Potion",
    value: 50
};

type Box<T> ={
    content:T;
};
const box: Box<string> ={
    content:"Sword"
};

type Status = "hp" | "mp" | "atk";

function updateStatus <T extends Record < Status, number>>(
    obj: T,
    key: Status,
    value: number
) {
    obj[key] = value;
}

interface Charecter {
    name: string;
    status: Record<"hp" | "mp", number>;
}
function damage< T extends Charecter> (char: T, amount: number) {
    char.status.hp -= amount;
}

interface player {
    name: string;
    hp:number;
    mp:number;
}
const sav: Partial<player> = {
    hp:80
};

type FullPlayer = Required<player>;

const confg: Readonly<{ volume: number}> = {
    volume:50
};

type Stateus = "hp" | "mp" | "atk";

const Status: Record < Stateus, number> = {
    hp:100,
    mp:30,
    atk:15
};

type playername = Pick<player,"name">;

type playerwithoutMP = Omit<player, "mp">;

type ACtion = "ATACK" | "HEAL" | "ESCAPE";
type BattleAction = Exclude<Action,"ESCAPE">;

type SpwciaSction =  Extract < Action, "ATTACK" | "HEAL">;

type MaybeNumber = number | null | undefined;
type SafeName = NonNullable < MaybeNumber>;

function createPlayer() {
    return { name: "Taro", hp: 100};
}
type PlayerType = ReturnType<typeof createPlayer>;

type plyer = {
    hp: number;
    mp: number;
    atk: number;
};
type ReadonlyPlayer = {
    [K in keyof player]: player[K];
};

type ReadonlyPlayr = {
    readonly [K in keyof player]: player[K];
};

type OptionalPlayer = {
    [K in keyof player]?: player[K];
};

type MyPartial<T> ={
    [K in keyof T]?:T[K];
};

type IsNumber<T> = T extends number ? "YES" : "NO";

type A = IsNumber<number>;
type B = IsNumber<string>;

type Return<T> = T extends (...ares: any[]) => infer R ? R : never;

type element <T> = T extends (infer U) [] ? U : never;
type d = element<number[]>;

type ToArray <T> = T extends any ? T[] : never;
type result = ToArray<string | number>;

type States = {
    hp: number;
    mp:number;
};

type StatusString <T> = {
    [K in keyof T ]: string ;
};
type StringString = StatusString<Status>;

type Act= "ATTACK" | "HEAL" | "ESCAPE";

function perform(action: ACtion) {

}

interface Profile {
    email?: string;
  }
  
  function sendEmail(profile: Profile) {
    if (!profile.email) return;
    console.log(profile.email.toLowerCase());
  }

interface Config {
    readonly apikey: string;
}
const Config: Config={ apikey:"12345"};

function gtValue<T,K extends keyof T> (obj: T, key: K){
    return obj[key];
}

const plyer ={ hp:100,mp:50};
getValue(plyer,"hp");

interface player {
    hp: number;
    mp: number;
    level: number;
}
function update(player:player,patch: Partial<player>) {
    if(patch.hp !== undefined) player.hp = patch.hp;
    if (patch.mp !== undefined) player.mp = patch.mp;
}

type IsString<T> = T extends string ? true: false;
type s = IsString<string>;
type S = IsString<number>;

type MaybNumber = number | null | undefined;
type SafeNameber = NonNullable<MaybNumber>;

let f: SafeNameber = 10;

type Stats = {
    hp: number;
    mp: number;
  };
  
type StringStatus = {
    [K in keyof Status]: string;
};

const playerStatus: StringStatus = { hp: "100", mp: "50" };

type sctu= "ATTACK" | "HEAL" | "ESCAPE";
type BattleActin = Exclude<Action,"ESCAPE">;
type HealAction = Extract<Action, "HEAL" | "ESCAPE">;

function reatePlayer() {
    return { name: "Taro",hp:100};
}
type PlayerTpe = ReturnType<typeof createPlayer>;
const newPlayer: PlayerType = createPlayer();

function isEven(num: number):String{
    return num % 2 === 0 ? "偶数":"奇数";
}
console.log(isEven(7));

//開始
//↓
//数値を入力
//↓
//数値 % 2 == 0 ?
//├─ Yes → 「偶数」と表示
//└─ No  → 「奇数」と表示
//↓
//終了

function maxOfThree(a:number,b:number,c:number):number{
    let max = a;
    if(b > max) max=b;
    if(c > max)max=c;
    return max;
}
console.log(maxOfThree(3,9,5));

//開始
//↓
//a, b, c を入力
//↓
//max = a
//↓
//b > max ?
//├ Yes → max = b
//└ No
//↓
//c > max ?
//├ Yes → max = c
//└ No
//↓
//max を表示
//↓
//終了

let sun=0;
for (let i =1;i <=10;i++) { 
    sun +=1
}
console.log(sun);
//開始
//↓
//sum = 0, i = 1
//↓
//i <= 10 ?
//├ Yes → sum = sum + i
//│       i = i + 1
//│       ↑ 繰り返す
//No
//↓
//sum を表示
//↓
//終了

function arrySum(arr:number[]):number{
    let num = 0;
    for (let i = 0; i< arr.length; i++) {
        num += arr[i];
    }
    return num;
}
console.log(arrySum([1,2,3,4,5]));
//開始
//↓
//配列を準備
//↓
//sum = 0, i = 0
//↓
//i < 配列の長さ ?
//├ Yes → sum += 配列[i]
//│       i++
//│       ↑ 繰り返す
//└ No
//↓
//sum を表示
//↓
//終了

function reverseNumber(num: number):number {
    let result = 0;

    while (num > 0) {
        result = result * 10 + (num % 10);
        num = Math.floor(num/10);
    }
    return result;
}
console.log(reverseNumber(123));

//開始
//↓
//数値を入力
//↓
//while 数値 > 0
//├ 余り = 数値 % 10
//├ 表示
//├ 数値 = 数値 / 10（整数）
//└ 繰り返し
//↓
//終了

function checkPassword(input: string):string{
    const correct = "secret";
    return input === correct ? "ログイン成功" : "エラー";
}
console.log(checkPassword("secret"));
//開始
//↓
//正しいパスワードを用意
//↓
//入力
//↓
//一致する？
//├ Yes → 「ログイン成功」
//└ No  → 「エラー」
//↓
//終了


function login(inputs: string[]): string {
    const correct = "pass";
    let attempts = 0;
  
    for (const input of inputs) {
      if (attempts >= 3) break;
  
      if (input === correct) {
        return "ログイン成功";
      }
      attempts++;
    }
    return "アカントロック";
  }
console.log(login(["aaa","bbb","pass"]));
//開始
//↓
//回数 = 0
//↓
//回数 < 3 ?
//├ Yes → パスワード入力
//│       一致？
//│       ├ Yes → 成功 → 終了
//│       └ No  → 回数++
//│               ↑ 繰り返す
//└ No
//↓
//「アカウントロック」
//↓
//終了


function finfvalue(arr:Number[],target:number): boolean {
    let found = false;

    for(const value of arr) {
        if(value === target){
            found = true;
            break;
        }
    }
    return found;
}
console.log(finfvalue([1,2,3,4,5],5));
//開始
//↓
//found = false
//↓
//配列を順に確認
//↓
//一致？
//├ Yes → found = true
//│       探索終了
//└ No
//↓
//found を表示
//↓
//終了


function grafe(score: number): string {
    if(score >= 90) return "A";
    if(score >= 70) return "B";
    return "C"; 
}
console.log(grafe(85));
//開始
//↓
//点数を入力
//↓
//90以上？
//├ Yes → A
//└ No → 70以上？
//        ├ Yes → B
//       └ No → C
//↓
//表示
//↓
//終了


function sumPositive(nums: number[]): number{
    let sum =0;
    for (const num of nums) {
        if(num === 0) break;
        if(num > 0) sum += num;
    }
    return sum;
}
console.log(sumPositive([3,-2,5,0,10]));
//開始
//↓
//sum = 0
//↓
//数値入力
//↓
//数値 == 0 ?
//├ Yes → 終了
//└ No → 数値 > 0 ?
 //       ├ Yes → sum += 数値
  //      └ No
//↓
//繰り返す
//↓
//sum 表示
//↓
//終了
