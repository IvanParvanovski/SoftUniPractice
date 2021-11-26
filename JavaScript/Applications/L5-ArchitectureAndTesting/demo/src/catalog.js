import { getAllMovies } from './api/data.js';
import { e, showSection } from './dom.js';

const catalogSection = document.getElementById('catalogSection');
const ul = catalogSection.querySelector('ul');
catalogSection.remove();

export function showCatalogPage() {
    showSection(catalogSection);
    loadMovies();
}

async function loadMovies() {
    ul.replaceChildren(e('p', {}, 'Loading...'));
    const movies = getAllMovies()
    ul.replaceChildren(...movies.map(createMovieCard));
}

function createMovieCard(movie) {
    return e('li', {}, movie.title);   
}
