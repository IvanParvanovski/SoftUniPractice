import { html, render } from '../node_modules/lit-html/lit-html.js';
import { movies } from './movieSeeder.js';

const tmp = (movies) => html`
<ul>
    ${movies.map(m => cardTmp(m))}
</ul>   
`;

const cardTmp = (movie) => html`
<li class="cards_item">
    <div class="card">
        <div class="card_image"><img src="./images/${movie.imageLocation}.jpg" alt="No Image">
        </div>
        <div class="card_content">
            <h2 class="card_title">${movie.title}</h2>
            <button class="showBtn" @click=${onClick}>Read More</button>
            <div class="movie" style="display:{?}" id="${movie.id}">
                <p class="card_text">${movie.description}</p>
            </div>  
        </div>
    </div>
</li>
`

const root = document.getElementById('allMovies');
page();

export function page() {
    render(tmp(movies, onClick), root);
    
    const cardsText = document.querySelectorAll('.card_text');
    for (const ct of cardsText) {
        ct.style.display = 'none';
    }
}

function onClick(event) {
    const contentDiv = event.target.parentNode; 
    
    const content = contentDiv.querySelector('.card_text');
    const btn = event.target;

    if (btn.textContent == 'Read More') {
        content.style.display = 'inline-block';
        btn.textContent = 'Read Less'
    } else if (btn.textContent == 'Read Less') {
        content.style.display = 'none';
        btn.textContent = 'Read More';
    }

    
}


