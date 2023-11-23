document.addEventListener("DOMContentLoaded", function () {
    var header = document.querySelector("header");
    var nav = document.querySelector("nav");
  
    window.addEventListener("scroll", function () {
      var scrollPosition = window.scrollY;
  
      if (scrollPosition > 100) {
        header.classList.add("scrolled");
        nav.classList.add("scrolled");
      } else {
        header.classList.remove("scrolled");
        nav.classList.remove("scrolled");
      }
    });
  });
  

