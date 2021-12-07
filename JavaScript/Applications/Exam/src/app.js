import { page, render } from './lib.js';
import { catalogPage } from './views/catalog.js';
import { detailsPage } from './views/details.js';
import { editPage } from './views/edit.js';
import { homePage } from './views/home.js';
import { loginPage } from './views/login.js';
import { registerPage } from './views/register.js';
import { logout } from './api/data.js';
import { searchPage } from './views/search.js';
import { createPage } from './views/create.js';
import { getUserData } from './util.js';

const root = document.getElementById('main-content');
const logoutBtn = document.getElementById('logout-btn');
logoutBtn.addEventListener('click', logoutUser);

updateNav();

page(decoratorPage);
page('/', homePage);
page('/catalog', catalogPage);
page('/create', createPage);
page('/login', loginPage);
page('/register', registerPage);
page('/details/:id', detailsPage);
page('/edit/:id', editPage);
page('/search', searchPage);
page.redirect('/index.html', '/');
page.start();

function decoratorPage(ctx, next) {
    ctx.render = (tmp) => render(tmp, root);
    ctx.updateNav = updateNav;
    
    next();
}

async function logoutUser(ev) {
    await logout();
    updateNav();
    page.redirect('/');
}

function updateNav() {
    const userBtns = [...document.querySelectorAll('.userBtn')];
    const guestBtns = [...document.querySelectorAll('.guestBtn')];
    const userData = getUserData();
    
    if (userData) {
        userBtns.forEach(b => b.style.display = 'inline');
        guestBtns.forEach(b => b.style.display = 'none');
    } else {
        userBtns.forEach(b => b.style.display = 'none');
        guestBtns.forEach(b => b.style.display = 'inline');
    }
}
