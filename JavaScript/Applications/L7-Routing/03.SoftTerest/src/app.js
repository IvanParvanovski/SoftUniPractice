import { render, page } from './utilities.js';
import { homePage } from './views/home.js';
import { catalogPage } from './views/catalog.js';
import { detailsPage } from './views/details.js';
import { loginPage } from './views/login.js';
import { registerPage } from './views/register.js';
import { createPage } from './views/create.js';

const root = document.getElementById('page-container');

async function decorateContext(ctx, next) {
    ctx.render = (tmp) => render(tmp, root);
    ctx.page = page;
    next();
}

page(decorateContext);
page('/home', homePage);
page('/catalog', catalogPage);
page('/details/:id', detailsPage);
page('/login', loginPage);
page('/register', registerPage);
page('/create', createPage);

page.redirect('/', '/home')
page.start();
