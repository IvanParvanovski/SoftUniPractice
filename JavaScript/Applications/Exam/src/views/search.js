import { searchAlbum } from '../api/data.js';
import { html, until } from '../lib.js';
import { getUserData } from '../util.js';

const albumCard = (album, props) => html`
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
        ${props.isLogged 
            ? html`
                <div class="btn-group">
                    <a href="/details/${album._id}" id="details">Details</a>
                </div>`
            : null
        }
    </div>
</div>`;

const searchTmp = (props, albums, onSearch) => html`
<section id="searchPage">
    <h1>Search by Name</h1>

    <div class="search">
        <input id="search-input" type="text" name="search" placeholder="Enter desired albums's name">
        <button @click=${onSearch} class="button-list">Search</button>
    </div>

    <h2>Results:</h2>
    ${!props.isStart 
        ? html`
            <div class="search-result">
                ${albums.length != 0 
                    ? albums.map(a => albumCard(a, props)) 
                    : html`<p class="no-result">No result.</p>`}
            </div>` 
        : null
    }

</section>`;

export function searchPage(ctx) {
    let albums = [];

    const props = {
        isStart: true,
        isLogged: (getUserData() != null)
    }

    ctx.render(searchTmp(props, albums, onSearch));

    async function onSearch(event) {
        const query = event.target.parentElement.querySelector('#search-input').value;
        
        if (query == '') {
            return alert('Please fill in the search field!');
        }
        
        albums = await searchAlbum(query);
        props.isStart = false;

        ctx.render(searchTmp(props, albums, onSearch));
    } 
}
