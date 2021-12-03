import { getUserData } from '../api/api.js';
import { deleteItem, getById } from '../api/data.js';
import { html, until } from '../lib.js';

const detailsTmp = (itemPromise) => html` 
<div class="row space-top">
    <div class="col-md-12">
        <h1>Furniture Details</h1>
    </div>
</div>
<div class="row space-top">
    ${until(itemPromise, html`<p>Loading &hellip;`)}
</div>`;

const itemTmp = (item, isOwner, onDelete) => html`
<div class="col-md-4">
    <div class="card text-white bg-primary">
        <div class="card-body">
            <img src="${item.img}" />
        </div>
    </div>
</div>
<div class="col-md-4">
    <p>Make: <span>${item.make}</span></p>
    <p>Model: <span>${item.model}</span></p>
    <p>Year: <span>${item.year}</span></p>
    <p>Description: <span>${item.description}</span></p>
    <p>Price: <span>${item.price}</span></p>
    <p>Material: <span>${item.material}</span></p>
    ${isOwner ? html`<div>
        <a href="/edit/${item._id}" class="btn btn-info">Edit</a>
        <a href="javascript:void(0)" @click=${() => onDelete(item._id)} class="btn btn-red">Delete</a> 
    </div>` : null}
</div>`;

export async function detailsPage(ctx) {
    ctx.render(detailsTmp(loadItem()));

    async function onDelete(id) {
        const choice = confirm('Are you sure you want to delete this item?')
        if (choice) {
            await deleteItem(id);
            ctx.page.redirect('/');
        }
    }

    async function loadItem() {
        const item = await getById(ctx.params.id);

        const userData = getUserData();
        const isOwner = userData.id == item._ownerId;

        return itemTmp(item, isOwner, onDelete);
    }
}
