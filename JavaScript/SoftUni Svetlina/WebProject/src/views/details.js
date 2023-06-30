import { html } from '../lib.js';
import { deleteAlbum, getAlbumById, register, login } from '../util.js';


const albumTmp = (ctx, album, logged, onDelete) => html`
<section id="album">
    <div id="album__content">
        <div class="content-section">
            <h2 class="content-section__heading">Artist</h2>
            <p class="content-section__text">${album.artist}</p>
        </div>

        <div class="content-section">
            <h2 class="content-section__heading">Genre</h2>
            <p class="content-section__text">${album.genre}</p>
        </div>

        <div class="content-section">
            <h2 class="content-section__heading">Name</h2>
            <p class="content-section__text">${album.name}</p>
        </div>

        <div class="content-section">
            <h2 class="content-section__heading">Release Date</h2>
            <p class="content-section__text">${album.releaseDate}</p>
        </div>

        ${logged
        ?
        html`<div class="controls">
            <button class="controls__edit">
                <a href="/edit/${album._id}">Edit</a>
            </button>
            <button class="controls__delete" @click=${(event) => onDelete(ctx)}>Delete</button>
        </div>`
        :
        html``
    }
        

        <!-- <div>
                    <h2>price</h2>
                    <p>7.33</p>
                </div> -->
    </div >
        <img id="album__img"
            src="${album.imgUrl}"
            alt="No Image">
    <div class="desc__div">
        <p id="album__desc">${album.description} CONTENT content CONTENT  CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT  CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENT CONTENT content CONTENTv</p>
    </div>
</section>
`

export async function albumPage(ctx) {

    let logged = false;
    let album = await getAlbumById(ctx.params.id);
    console.log(album);

    const userData = JSON.parse(sessionStorage.getItem('userData'));
    if (userData != undefined) {
        logged = userData.id == album._ownerId;
    }

    ctx.render(albumTmp(ctx, album, logged, onDelete));
}

async function onDelete(ctx) {
    const choice = confirm('Are you sure you want to delete it?');

    if (choice) {
        console.log(ctx.params.id);
        await deleteAlbum(ctx.params.id);
        ctx.page.redirect('/catalogue');
    }
}
