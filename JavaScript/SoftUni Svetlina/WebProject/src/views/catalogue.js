import { html } from '../lib.js';
import { cardHover } from '../scripts/card-hover.js';
import { getAllAlbums, logout } from '../util.js';


const catalogueTmp = (albums, isLogged) => html`
    ${albums.length != 0
        ? cataloguesAlbumsTmp(albums, isLogged)
        : html`<h2 class="missing-text">No Albums in Catalog!</h2>`
    }
`;

const cataloguesAlbumsTmp = (albums, isLogged) => html`
    <section id="banner" class="--half">
        <div class="background">
            <img class="background__img"
                src="https://images.unsplash.com/photo-1491421722235-b556e8f64dab?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NTh8fGFsYnVtc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=2000&q=60"
                alt="No Image">
            <div class="background__gradient"></div>
        </div>
    
        <h1 class="banner__title">Albums Catalogue</h1>
    </section>

    ${isLogged
        ?
        html` 
        <section class="card-creation">
            <h3 class="card-creation__heading" class>Create New Album</h3>
            <span>|</span>
            <button class="card-creation__button">
                <a class="card-creation__link" href="/create">Create</a>
            </button>
        </section>`
        :
        html``
    }

    <section class="cards">
        ${albums.map(a => cardTmp(a, isLogged))}
    </section>
   
`

const cardTmp = (album, isLogged) => html`
<article class="card">
    <img class="card__img" src="${album.imgUrl}" alt="No Image">

    <div class="desc">
        <div class="desc__gradient"></div>

        <div class="content">
            <h1 class="desc__content__artist">
                ${album.artist}
            </h1>

            <h2 class="desc__content__name">
                ${album.description}
            </h2>

            <div class="controls">
                <h2 class="desc__content__price">
                    $${album.price}
                </h2>

                <button>
                    <a class="desc__content__view-more" href="/details/${album._id}">View More</a>
                </button>
            </div>
        </div>
    </div>

</article>`;

export async function cataloguePage(ctx) {
    let albums = [];

    try {
        albums = await getAllAlbums();
    } catch (err) {
        console.log(err);
    }

    const userData = JSON.parse(sessionStorage.getItem('userData'));
    
    const isLogged = userData != undefined;


    ctx.render(catalogueTmp(albums, isLogged));
    cardHover();
}