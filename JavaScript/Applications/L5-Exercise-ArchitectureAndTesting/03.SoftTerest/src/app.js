import { showSection } from './dom.js';
import { showHomePage } from './views/home.js'
import { showCatalogPage } from './views/catalog.js';
import { showCreatePage } from './views/create.js';
import { showLoginPage } from './views/login.js';
import { showRegisterPage } from './views/register.js';
import { showDetailsPage } from './views/details.js';
import { logout } from './api/api.js';

const links = {
    'homeLink': 'home',
    'getStartedLink': 'home', 
    'catalogLink': 'catalog',
    'createLink': 'create',
    'loginLink': 'login',
    'registerLink': 'register',
};

const views = {
    'home': showHomePage,
    'catalog': showCatalogPage,
    'create': showCreatePage,
    'login': showLoginPage,
    'register': showRegisterPage,
    'details': showDetailsPage,
};

const nav = document.querySelector('nav');
nav.addEventListener('click', onNavigate);
document.getElementById('logoutBtn').addEventListener('click', async (ev) => {
    ev.preventDefault();

    await logout();
    updateNav();
    goTo('home');
});

const ctx = {
    goTo,
    showSection,
    updateNav,
}

// Start application in home view
goTo('home');
updateNav();

function onNavigate(event) {
    const name = links[event.target.id];

    if (name) {
        event.preventDefault();
        goTo(name);
    }
}

function goTo(name, ...params) {
    const view = views[name];

    if (typeof view == 'function') {
        view(ctx, ...params);
    }
}

function updateNav() {
    const userData = JSON.parse(sessionStorage.getItem('userData'));
    const userLinks = [...nav.querySelectorAll('.user')];
    const guestLinks = [...nav.querySelectorAll('.guest')];

    if (userData != null) {
        userLinks.forEach(l => l.style.display = 'block');
        guestLinks.forEach(l => l.style.display = 'none');
    } else {
        userLinks.forEach(l => l.style.display = 'none');
        guestLinks.forEach(l => l.style.display = 'block');
    }
}
