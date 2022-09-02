// myFunc.js

var su = 13;
let su2 = 1004;

console.log(su + su2);

function good(){
    console.log("좋아요 !");
}

window.onload = function(){
    let btnGood = document.querySelector("#goodBtn");
    btnGood.addEventListener("click", function(){
        console.log("GOOD 아주 좋아용");
    })
}

function hello(){
    console.log("참조형 함수 hello");
}