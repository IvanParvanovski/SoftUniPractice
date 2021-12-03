import { getUserData } from './api/api.js';
import { logout } from './api/data.js';
import { render, page } from './lib.js';
import { catalogPage } from './views/catalog.js';
import { createPage } from './views/create.js';
import { detailsPage } from './views/details.js';
import { editPage } from './views/edit.js';
import { loginPage } from './views/login.js';
import { registerPage } from './views/register.js';

const root = document.querySelector('div.container');
const logoutBtn = document.getElementById('logoutBtn');
logoutBtn.addEventListener('click', onLogout);

updateUserNav();
page(decorateContext);
page('/', catalogPage);
page('/details/:id', detailsPage);
page('/create', createPage);
page('/edit/:id', editPage);
page('/login', loginPage);
page('/register', registerPage);
page('/my-furniture', catalogPage);

page.start();

function decorateContext(ctx, next) {
    ctx.render = (content) => render(content, root);
    ctx.updateUserNav = updateUserNav;
    
    next();
}

function updateUserNav() {
    const userData = getUserData();
    const guestBtns = document.getElementById('guest');
    const userBtns = document.getElementById('user');

    if (userData) {
        userBtns.style.display = 'inline-block';
        guestBtns.style.display = 'none';
    } else {
        userBtns.style.display = 'none';
        guestBtns.style.display = 'inline-block';
    }

}

async function onLogout(event) {
    await logout();
    updateUserNav();
    page.redirect('/');
}

