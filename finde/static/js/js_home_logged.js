
const tog_menu = document.querySelector(".dropMenu-toggle");
const tog_ntf = document.querySelector(".ntfMenu-toggle");

tog_menu.addEventListener("click", function (){
    this.classList.toggle("active");
})

tog_ntf.addEventListener("click", function () {
    this.classList.toggle("active");
})

console.log("que mierda")
