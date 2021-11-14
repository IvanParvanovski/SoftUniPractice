import { e, showSection } from './dom.js';

const catalogSection = document.getElementById('catalogSection');
catalogSection.remove();

const ul = catalogSection.querySelector('ul');

export function showCatalogPage() {
    showSection(catalogSection);
    loadMovies();
}

async function loadMovies() {
    ul.replaceChildren(e('p', {}, 'Loading...'));
    
    const options = {method: 'get', headers: {}};
    const token = sessionStorage.getItem('token');

    if (token != null) {
        options.headers['X-Authorization'] = token;
    }

    const res = await fetch('http://localhost:3030/data/movies');
    const movies = await res.json();

    ul.replaceChildren(...movies.map(createMovieCard));
}

function createMovieCard(movie) {
    return e('li', {}, movie.title);   
}
