import { getAll } from '../api/data.js';
import { html } from '../lib.js';
import { getUserData } from '../util.js';

const albumCard = (album, isLogged) => html`
<div class="card-box">
    <img src=${album.imgUrl}>
    <div>
        <div class="text-center">
            <p class="name">Name: ${album.name}</p>
            <p class="artist">Artist: ${album.artist}</p>
            <p class="genre">Genre: ${album.genre}</p>
            <p class="price">Price: $${album.price}</p>
            <p class="date">Release Date: ${album.releaseDate}<p>
        </div>

        ${isLogged 
            ? html`
                <div class="btn-group">
                    <a href="/details/${album._id}" id="details">Details</a>
                </div>`
            : null
        }
    </div>
</div>`;

const catalogTmp = (albums, isLogged) => html`
<section id="catalogPage">
    <h1>All Albums</h1>

    ${albums.length != 0 ? albums.map(a => albumCard(a, isLogged)) : html`<p>No Albums in Catalog!</p>`}
    
</section>`;

export async function catalogPage(ctx) {
    let albums = await getAll();
    const isLogged = getUserData() != null;

    ctx.render(catalogTmp(albums, isLogged));
}
