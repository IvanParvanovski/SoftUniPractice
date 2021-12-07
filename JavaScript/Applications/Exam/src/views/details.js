import { deleteAlbum, getById } from '../api/data.js';
import { html } from '../lib.js';
import { getUserData } from '../util.js';

const detailsTmp = (album, isOwner, onDelete) => html`
<section id="detailsPage">
    <div class="wrapper">
        <div class="albumCover">
            <img src=${album.imgUrl}>
        </div>
        <div class="albumInfo">
            <div class="albumText">

                <h1>Name: ${album.name}</h1>
                <h3>Artist: ${album.artist}</h3>
                <h4>Genre: ${album.genre}</h4>
                <h4>Price: $${album.price}</h4>
                <h4>Date: ${album.releaseDate}</h4>
                <p>Description: ${album.description}</p>
            </div>

            <!-- Only for registered user and creator of the album-->
            ${isOwner ? html`
            <div class="actionBtn">
                <a href="/edit/${album._id}" class="edit">Edit</a>
                <a href="javascript:void(0)" class="remove" @click=${onDelete}>Delete</a>
            </div>` : null}
        </div>
    </div>
</section>`;

export async function detailsPage(ctx) {
    const album = await getById(ctx.params.id);
    const user = getUserData();
    let isOwner = false;

    if (user) {
        isOwner = album._ownerId == user.id;
    }

    ctx.render(detailsTmp(album, isOwner, onDelete));

    async function onDelete(event) {
        const choice = confirm('Are you sure you want to delete it?');

        if (choice) {
            await deleteAlbum(ctx.params.id);
            ctx.page.redirect('/catalog');
        }
    }
}
