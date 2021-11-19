import { showView, e } from './src/dom.js';
import { showCreate } from './src/create.js';
import { showDetails } from './src/details.js';

const homeSection = document.getElementById('home-page');
const addMovieBtn = homeSection.querySelector('#add-movie-button').querySelector('a');
const catalog = homeSection.querySelector('#movie .card-deck');

addMovieBtn.addEventListener('click', showCreate);
homeSection.remove();

showHome();

catalog.addEventListener('click', (event) => {
    let target = event.target;

    if (target.tagName == 'BUTTON') {
        target = target.parentElement;
    }

    if (target.tagName != 'A') {
        return;
    }

    const id = target.dataset.id;
    showDetails(id);
});

export function showHome() {
    showView(homeSection);

    loadMovies();
}

async function loadMovies() {
    catalog.replaceChildren(e('p', {}, 'Loading...'));

    const movies = await getMovies();
    catalog.replaceChildren(...movies.map(m => createMovieCard(m)));

}

function createMovieCard(movie) {
    const element = e('div', {'className': 'card mb-4'});
    
    element.innerHTML = [
        `<img class="card-img-top" src="${movie.img}" alt="Card image cap" width="400">`,
        '<div class="card-body">',
            `<h4 class="card-title">${movie.title}</h4>`,
        '</div>',
        '<div class="card-footer">',
            `<a data-id="${movie._id}" href="#">`,
                `<button type="button" class="btn btn-info">Details</button>`,
            '</a>',
        '</div>',
    ].join('');

    return element;
}

async function getMovies() {
    const response = await fetch('http://localhost:3030/data/movies'); 
    try {
        if (response.ok == false) {
            throw new Error(`${response.status} ${response.statusText}`);
        }
    
        const movies = await response.json();
    
        return movies;
    } catch (err) {
        alert(err);
    }
}
