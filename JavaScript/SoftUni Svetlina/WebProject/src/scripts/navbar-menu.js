import { getUserData } from '../util.js';


window.onresize = onResize;

let open = false;
let visibleSection;
let reset = false;

const navbarLinks = document.querySelector('.links-section');
const guestSection = document.querySelector('.guest-section');
const userSection = document.querySelector('.user-section');

const navbarBars = document.querySelector('.navbar__controls .fa-bars');
const navbarXmark = document.querySelector('.navbar__controls .fa-xmark');

navbarBars.addEventListener('click', onToggle);
navbarXmark.addEventListener('click', onClose);

function onToggle(event) {    
    open = true;
    navbarBars.style.display = 'none';
    navbarXmark.style.display = 'inline-block';

    navbarLinks.style.display = 'flex';
    visibleSection.style.display = 'flex';
}

function onClose(event) {
    open = false;
    navbarBars.style.display = 'inline-block';
    navbarXmark.style.display = 'none';
    
    navbarLinks.style.display = 'none';
    visibleSection.style.display = 'none';
}

export function updateNav(redirected) {
    const navbarUsername = document.querySelector('.user-section__name');
    
    const userData = JSON.parse(sessionStorage.getItem('userData'));
    const isLogged = userData != undefined;


    if (isLogged) {
        visibleSection = userSection;
    } else {
        visibleSection = guestSection;
    }

    onRedirect(redirected);
    onResize();
    const data = getUserData();
    
    if (data != undefined) {
        navbarUsername.textContent = data.email;
    }
}

function onResize() {
    if (window.innerWidth == 1080) { reset = false; }
    if (reset) { resetView(); }

    if (window.innerWidth < 1080) {
        navbarLinks.style.display = open ? 'flex' : 'none';
        visibleSection.style.display = open ? 'flex' : 'none';
    } else {
        visibleSection.style.display = 'flex';
        navbarLinks.style.display = 'flex';
    }
}

function onRedirect(redirected) {
    if (redirected) {
        userSection.style.display = 'none';
        guestSection.style.display = 'none';
        onClose();
    }
}

function resetView() {
    reset = true;
    navbarLinks.style.display = 'none';
    visibleSection.style.display = 'none';
}
