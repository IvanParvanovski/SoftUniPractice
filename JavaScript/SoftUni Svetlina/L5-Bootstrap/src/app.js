import { page, render } from './lib.js';
import { catalogPage } from './views/catalog.js';
import { detailsPage } from './views/details.js';
import { homePage } from './views/home.js';
import { loginPage } from './views/login.js';
import { profilePage } from './views/profile.js';
import { registerPage } from './views/register.js';

const root = document.getElementById('root');

updateNav();
page(decoratorContext);
page('/', homePage);
page('/catalog', catalogPage);
page('/register', registerPage);
page('/login', loginPage);
page('/profile/:id', profilePage);
page('/details/:id', detailsPage);
page.redirect('/index.html', '/')
page.start();

function decoratorContext(ctx, next) {
    ctx.render = (tmp) => render(tmp, root);
    ctx.updateNav = updateNav;
    next();
}

function updateNav() {
    const userData = sessionStorage.getItem('userData');

    const userBtns = [...document.getElementsByClassName('user')];
    const guestBtns = [...document.getElementsByClassName('guest')];

    if (userData != null) {
        userBtns.map(b => b.style.display = 'inline');
        guestBtns.map(b => b.style.display = 'none');
    } else {
        userBtns.map(b => b.style.display = 'none');
        guestBtns.map(b => b.style.display = 'inline');
    }
}