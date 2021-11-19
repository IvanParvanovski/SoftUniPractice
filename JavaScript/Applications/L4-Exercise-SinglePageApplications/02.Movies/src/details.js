import { showView } from './dom.js';
import { showEdit } from './edit.js';

const detailsSection = document.getElementById('movie-details');
detailsSection.remove();

const editBtn = detailsSection.querySelector('#editBtn');
editBtn.addEventListener('click', showEdit);


export function showDetails(movieId) {
    showView(detailsSection);
}
