import { showCatalog } from './views/catalog.js';
import { showCreate } from './views/create.js';
import { showUpdate } from './views/update.js';
import { render } from './views/lib.js';

const root = document.querySelector('body');

const ctx = {
    update,
};

update();

function update() {
    render([
        showCatalog(ctx),
        showCreate(ctx),
        showUpdate(ctx),
    ], root);
}
