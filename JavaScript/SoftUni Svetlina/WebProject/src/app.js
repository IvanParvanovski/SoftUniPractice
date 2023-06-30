import { page, render } from './lib.js';
import { logout } from './util.js';
import { cataloguePage } from './views/catalogue.js';
import { createPage } from './views/create.js';
import { albumPage } from './views/details.js';
import { editPage } from './views/edit.js';
import { homePage } from './views/home.js';
import { loginPage } from './views/login.js';
import { registerPage } from './views/register.js';
import { updateNav } from './scripts/navbar-menu.js';

const root = document.querySelector('main');
const logoutBtn = document.getElementById('logout-btn');
logoutBtn.addEventListener('click', logoutUser);
export let authenticationSection;


// Starwars
const webAPI = await fetch('https://swapi.dev/api/planets/3/?format=json').then((x) => x.json());
console.log(webAPI);


page(decoratorPage);
page('/', homePage);
page('/catalogue', cataloguePage);
page('/details/:id', albumPage);
page('/login', loginPage);
page('/register', registerPage);
page('/edit/:id', editPage);
page('/create', createPage);

page.redirect('/index.html', '/');

page.start();


function decoratorPage(ctx, next) {
    ctx.render = (tmp) => render(tmp, root);
    ctx.updateNav = updateNav;
    
    updateNav(true);
    next();
}

async function logoutUser(ev) {
    await logout();
    updateNav(true);
    page.redirect('/');
}


