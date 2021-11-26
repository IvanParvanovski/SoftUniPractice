import { showButtons } from './dom.js';
import { showHomePage } from './home.js';
import { showAboutPage } from './about.js';
import { showCatalogPage } from './catalog.js';
import { showLoginPage } from './login.js';
import { showRegisterPage } from './register.js';
import { logout } from './api/data.js';

const sections = {
    homeBtn: showHomePage,
    catalogBtn: showCatalogPage,
    aboutBtn: showAboutPage, 
    loginBtn: showLoginPage,
    registerBtn: showRegisterPage,
    logoutBtn: logoutUser,
};

document.querySelector('nav').addEventListener('click', onNavigate);

// Start application in home view
showHomePage();
showButtons();

function onNavigate(event) {
    if (event.target.tagName != 'A') {
        return;
    }

    const view = sections[event.target.id];

    if (typeof view == 'function') {
        event.preventDefault();
        view();
        showButtons();
    }

}

async function logoutUser(event) {
    await logout();
    
    await fetch('http://localhost:3030/users/logout', {
        method: 'post',
        headers: {
            'X-Authorization': sessionStorage.getItem('token')
        } 
    });

    sessionStorage.removeItem('token');
}

