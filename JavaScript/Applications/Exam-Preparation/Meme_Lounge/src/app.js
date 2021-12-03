import { page, render } from './lib.js';
import { catalogPage } from './views/catalog.js';
import { createPage } from './views/create.js';
import { detailsPage } from './views/details.js';
import { editPage } from './views/edit.js';
import { homePage } from './views/home.js';
import { loginPage } from './views/login.js';
import { registerPage } from './views/register.js';
import { userProfilePage } from './views/user-profile.js';
import { getUserData } from './util.js';
import { logout } from './api/data.js';
import * as not  from './notify.js';

const root = document.querySelector('main');
const logoutBtn = document.getElementById('logout-btn');
logoutBtn.addEventListener('click', logoutUser);

updateNav();

page(decoratorPage);
page('/', homePage)
page('/catalog', catalogPage);
page('/login', loginPage);
page('/register', registerPage);
page('/create', createPage);
page('/details/:id', detailsPage);
page('/edit/:id', editPage);
page('/profile/:id', userProfilePage);
page.start();

function decoratorPage(ctx, next) {
    ctx.render = (tmp) => render(tmp, root);
    ctx.updateNav = updateNav;

    next();
}

function updateNav() {
    const userData = getUserData();
    const usersBtns = document.querySelector('nav .user'); 
    const guestBtns = document.querySelector('nav .guest');

    if (userData) {
        usersBtns.style.display = 'block';
        guestBtns.style.display = 'none';
        document.getElementById('welcome-msg').textContent = `Welcome, ${userData.email}`;
    } else {
        usersBtns.style.display = 'none';
        guestBtns.style.display = 'block';
    }
}

async function logoutUser() {
    await logout();
    updateNav();
    page.redirect('/');
}
