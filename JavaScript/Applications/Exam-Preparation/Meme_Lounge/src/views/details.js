import { deleteMeme, getMemeById } from '../api/data.js';
import { html } from '../lib.js';
import { getUserData } from '../util.js';

// Details Meme Page (for guests and logged users)

const detailsTmp = (meme, isOwner, onDelete) => html`
<section id="meme-details">
    <h1>Meme Title: ${meme.title}
    </h1>
    <div class="meme-details">
        <div class="meme-img">
            <img alt="meme-alt" src=${meme.imageUrl}>
        </div>
        <div class="meme-description">
            <h2>Meme Description</h2>
            <p>${meme.description}</p>

            ${isOwner 
                ? html`<a class="button warning" href="/edit/${meme._id}">Edit</a>
                  <button class="button danger" @click=${(ev) => onDelete(meme._id)}>Delete</button>`
                : null
            }
            <!-- Buttons Edit/Delete should be displayed only for creator of this meme  -->
            
        </div>
    </div>
</section>`;

export async function detailsPage(ctx) {
    const meme = await getMemeById(ctx.params.id);
    const userData = getUserData();

    let isOwner = false;
    if (userData) {
        isOwner = meme._ownerId == userData.id;
    }

    ctx.render(detailsTmp(meme, isOwner, onDelete));

    async function onDelete(id) {
        const choice = confirm('Are you sure you want to delete it?');

        if (choice) {
            await deleteMeme(id);
            ctx.page.redirect('/catalog')
        }
    }
}

