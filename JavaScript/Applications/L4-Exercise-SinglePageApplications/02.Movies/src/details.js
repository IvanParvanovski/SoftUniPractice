import { e, showView } from './dom.js';
import { showEdit } from './edit.js';

const detailsSection = document.getElementById('movie-details');
detailsSection.remove();

const editBtn = detailsSection.querySelector('#editBtn');
editBtn.addEventListener('click', showEdit);


export async function showDetails(movieId) {
    const movie = await getMovie(movieId);
    detailsSection.replaceChildren(createDetails(movie));
    
    showView(detailsSection);
}

function createDetails(movie) {
    const controls = e('div', { className: 'col-md-4 text-center' },
        e('h3', { className: 'my-3' }, 'Movie Description'),
        e('p', {}, movie.description),
    );

    const userData = JSON.parse(sessionStorage.getItem('userData'));
    if (userData != null) {
        controls.appendChild(e('a', {className: 'btn btn-danger', href: '#'}));
    }

    const element = e('div', {className: 'container'}, 
        e('div', {className: 'row bg-light text-dark'}, 
            e('h1', {}, `Movie title: ${movie.title}`),
            e('div', { className: 'col-md-8' },
                e('img', { 
                    className: 'img-thumbnail',
                    src: movie.img,
                    alt: "Movie"
            })),
            controls
        )
    );

    return element;

    divEl.innerHTML = [
            '<a class="btn btn-danger" href="#">Delete</a>',
            '<a id="editBtn" class="btn btn-warning" href="#">Edit</a>',
            '<a class="btn btn-primary" href="#">Like</a>',
            '<span class="enrolled-span">Liked 1</span>',
        '</div>',
    ].join('');
      
    return divEl;
}

async function getMovie(id) {
    try {
        const res = await fetch('http://localhost:3030/data/movies/' + id);
        if (res.ok == false) {
            const err = res.json();
            throw new Error(err.message);
        }
    
        const data = await res.json();
        return data;
    } catch (err) {
        alert(err);
    }
}