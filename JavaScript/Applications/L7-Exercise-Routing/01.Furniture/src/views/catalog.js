import { html, until } from '../lib.js';
import { getAll, getMyItems } from '../api/data.js';
import { getUserData } from '../api/api.js';

const furnitureCardTmp = (item) => html`
<div class="col-md-4">
    <div class="card text-white bg-primary">
        <div class="card-body">
            <img src="${item.img}" />
            <p>${item.description}</p>
            <footer>
                <p>Price: <span>${item.price}</span></p>
            </footer>
            <div>
                <a href="/details/${item._id}" class="btn btn-info">Details</a>
            </div>
        </div>
    </div>
</div>`;

const catalogTmp = (dataPromise) => html`
<div class="row space-top">
    <div class="col-md-12">
        <h1>Welcome to Furniture System</h1>
        <p>Select furniture from the catalog to view details.</p>
    </div>
</div>
<div class="row space-top">
    ${until(dataPromise, html`<p>Loading &hellip;`)}
</div>`;

export async function catalogPage(ctx) {
    const userPage = ctx.pathname == '/my-furniture';

    ctx.render(catalogTmp(loadItems(userPage)));
}

async function loadItems(userPage) {
    let items = [];

    if (userPage) {
        const userId = getUserData().id;
        items = await getMyItems(userId);
    } else {
        items = await getAll();
    }

    return items.map(furnitureCardTmp);
}
