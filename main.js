const menuBtn = document.querySelector(".menu__btn");
const menuList = document.querySelector(".menu__list");
function toggleMenuVisibility() {
  menuList.classList.toggle("hide");
}
menuBtn.addEventListener("click", toggleMenuVisibility);

// Скрипт для раскрытия блока portfolio

const portBtn = document.querySelector(".portfolio__btn");
const labs = document.querySelector(".port__labs");
function showPort() {
  labs.classList.toggle("hide");
}
portBtn.addEventListener("click", showPort);

showPort();
const lab1Btn = document.querySelector("#lab__btn1");
const labs1 = document.querySelector(".lab1info");
function showLab1() {
  labs1.classList.toggle("hide");
}
lab1Btn.addEventListener("click", showLab1);
showLab1();

const lab2Btn = document.querySelector("#lab__btn2");
const labs2 = document.querySelector(".lab2info");
function showLab2() {
  labs2.classList.toggle("hide");
}
lab2Btn.addEventListener("click", showLab2);
showLab2();
