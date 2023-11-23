


/* =========== Show Navbar =========== */
const navbar = document.querySelector(".navbar");
const postloader = document.querySelector(".postloader");

postloader.addEventListener("click", () => {
  navbar.classList.toggle("show");
});



/* =========== Preloader =========== */
const preloader = document.querySelector(".preloader");

window.addEventListener("load", () => {
  setTimeout(() => {
    preloader.style.display = "none";
  }, 2000);
});

