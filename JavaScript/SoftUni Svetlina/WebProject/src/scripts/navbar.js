const nav = document.getElementsByTagName('nav')[0];
const navUl = document.querySelector('#navbar');

let lastScrollY = window.scrollY;

window.addEventListener('scroll', () => {

    if (window.scrollY > 128 && lastScrollY < window.scrollY) {
        nav.classList.add('nav--hidden');
    } else {
        nav.classList.remove('nav--hidden');
    }
    lastScrollY = window.scrollY;
});