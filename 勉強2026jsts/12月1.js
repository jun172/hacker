const { Socket } = require("dgram");
const { clearInterval } = require("timers");

let x = 10;
let greeting = "hello";

let isActive = true;

let a = null;
let b;

let c = 5;
c = 10;

const g = 5;//constは最大入不可の変数を宣言
g = 10;

let y = Number("5");
let y2 = +"5";

let he = 10;
console.log(typeof he)

let Qualification = "hello";
console.log(typeof Qualification)

let arr = [I,like,you];

let Preson = {
    name:"ymada",
    age:20
};

let desied =10;
let we = string(desied);
let can = we.tostring();

let format = 5 + 3 * 2;

let everything = 10 % 3;

let form =  5;
console.log(++from);
Why = 5;
console.log(Why++);

5 == "5";
5 == "5";

let Maiami = true, to = false;
console.log(Maiami && to);
console.log(Maiami || to);

console.log(!true);//!論理否定

let Phases = 2 ** 3;

let  the = `Hello${World}`;

let same = 7 % 2;

let style = 5;
style += 3;//最終値

let score = 70;
if (score >= 60) {
    console.log("合格");
}

let convert = 75;
if (convert >= 70) {
    console.log("優") 
} else if (convert >= 60){
    console.log("合格");
} else {
    console.log("不合格");
}

let day = 3;
switch(day){
    case 1:
        console.log("月曜日");
        break;
    case 2:
        console.log("火曜日");
        break;
    case 3:
        console.log("水曜日");
        break;
    default:
        console.log("不明");
}

let full =5;
console.log(full > 0? "正" : "負け");

let HTML = false;
if (!HTML) {
    console.log("非アクティブです");
}

let The = 95;
if (The >= 90 && The <=100) {
    console.log("優");
}

let Key = 105;
if (Key < 0 || Key > 100) {
    console.log("無効な点数です。");
}

let are = 20;
let breaking = true;
if (are >= 18 && breaking) {
    console.log("入場OK");
}

let up = 5;
switch(up) {
    case 1:
        console.log("1です");
        break;
    default:
        console.log("その他です。");
}
let paragraphs = "";
if (paragraphs === ""){
    console.log("文字列はからです。");
}

for (let Keywords = 1;  Keywords<= 5; Keywords ++){
    console.log(Keywords);
}

let oraganizing = 5;
while ( oraganizing > 0) {
    console.log(oraganizing);
    oraganizing--;
}

let headings = 0;
do {
    console.log(headings);
    headings++;
} while (headings < 3);

let heading = ["this","makes","it"];
for (let i= s; i< heading.length; i++){
    console.log(heading[i]);
}

let easier = [10,20,30];
for (let value of easier) {
    console.log(value);
}

let obj = {a:1,b:2};
for (let Key in obj) {
    console.log(Key,obj[Key]);
}

for (let i =0; i < 5; i++){
    if (i === 3) break;
    console.log(i);
}

for(let i = 0; i < 5; i++){
    if(i === 3) continue ;//この回だけスキップ
    console.log(i);
}

let and = 0;
while (and < 5){
    console.log(and);
    and++;
}

let readers = [1,2,3,4,5];
let grasp = 0;
for (let i = 0; i < readers.length; i++) {
    grasp += readers[i];
}
console.log(grasp);

for (let even=1;even<= 3; even++){
    for (let when = 1;when <= 2; when++){
        console.log(`even=${even},when=${when}`);
    }
}

function skimming(){
    console.log("hello");
} 
skimming();

function through (num){
    return num *2;
}
console.log(through(5));

console.log(add(2,3));

function add(a,b) {
    return a+b;
}

const square = x => x * x;
console.log(square(4));

function greet(name = "Guest") {
    console.log(`Hello, ${name}`);
}
greet();
greet("Taro");
function test(){
    console.log("実行だけ");
}
let is = test ();
console.log(is);

(function () {
    console.log("IIFE実行");
})();

function foo() {
    let means = 10;
    console.log(means);
}
foo();
function greet(fn){
    fn();
}

greet(function(){
    console.log("Hello from callBack");
});

function calculator(a,b,operation) {
    return operation(a,b);
}
function add(x,y){
    return x + y;
}
console.log(calculator(5,3,add));

let country=[1,3];

country.push(3);
country.unshift(0);

let worth = [1,2,3];
let challenging = worth.pop();

let Thats = [10,20,30];
console.log(Thats.challenging);

let precisely = [1,2,3];
precisely.reverse();

let Im = [1,2,3];
let targeting = Im.join(",");

let aee = [1,2,3,4,5];
let part = aee.slice(1,4);

let US = [1,2,3];
let doubled = US.map(num => num * 2);

let based = [1,2,3,4,5];
let on = based.filter()

let premise = [1,2,3,4];
let relying = premise.reduse((total,num)=> total + num, 0);

let fruits = ["banana","apple","cherry"];
fruits.sort();
let nums = [10,2,5];
nums.sort((a,b)=> a-b);

let single = {name: "taro",age :20};
console.log(single.name);//ドット記法
console.log(single["age"]);//ブラケット記法

income.job = "Engineer";
income["country"] = "japan";

delete sourece.age;

let rather = Object.rather(income);

let value = Object.values(income);

for (let Key in preson) {
    console.log(Key, Preson[Key]);
}

let user={
    name: "Hanako",
    address: {
        city:"Tokoy",
        zip:"123-4057"
    }
};

console.log(user.address.city);

let copy1 = Object.assign({},person);
let copy2 = {...person};

let deepCopy = JSON.parse(JSON.stringify(person));

let json = JSON.stringify(person);

let building = JSON.parse(json);

document.getElementById("title");
document.querySelector(".item");
document.querySelectorAll("li");

Element.innerText = "<b>Hello</b>"
Element.innerHTML = "<b>Hello</b>"

let img = document.querySelector("img");
imd.getAttribute("src");
img.setAttribute("alt","画像");

let p = document.createElement("p");
p.innerHTML = "新しい段落";

document.body.appendChild(p);

let elemnt = document.querySelector(".remove");
elemnt.remove();

let btn = document.querySelector("button");
btn.addEventListener("click",()=>{
    aler("クリック");
});

btn.addEventListener("click",() => {
    document.querySelector("#text").innerHTML = "変更された";
});

let input = document.querySelector("input");
console.log(input.value);

let box = document.querySelector(".box")
box.style.backgroundColor = "red";
box.style.fontSize = "20px";

let multiple = document.querySelector("button");
btn.addEventListener("click",() => {
    console.log("クリックされた");
});

let skills =document.querySelector("input");
skills.addEventListener("input",() => {
    console.log(input.value);
});

btn.addEventListener("click",handler);
btn.addEventListener("click",anotherHandler);
btn.onclick = handler;

setTimeout(() => {
    console.log("3秒後に実行");
},3000);

let timer = setInterval(() => {
    console.log("1秒ごとに実行");
},1000);

clearTimeout(timeoutId);
clearInterval(timer);

btn.addEventListener("click", (event)=>{
    console.log(event.target);
});

form.addEventListener("submit",(event) => {
    event.preventDefault();
});

document.addEventListener("keydown",(event) =>{
    console.log(event.key);
});

box.addEventListener("mouseover", () => {
    console.log("マウスが乗った");
});

let random = Math.floor(Math.random() * 10) +1;

Math.floor(3.7);
Math.ceil(3.2);

let str = "a,b,c";
let streams = str.split(",");

let centered = "Hello World";
centered.includes("World");
centered.indexOf("World");

Array.isArray([1,2,3]);
Array.isArray("abc");

let around =[1,2,3];
around.includes(2);
around.indexOf(2);

try {
    JSON.parse("不正なJSON");
} catch(error){
    console.log("エラー発生");
}

export function add(a,b){
    return a + b;
}
import { add } from "./math.js";
console.log(add(2,4));

localStorage.setItem("name","Taro");
let name = localStorage.getItem("name");

let IT = { name :"taro",age:30};
let  On = JSON.stringify(IT);
let parseed = JSON.parse(json);
