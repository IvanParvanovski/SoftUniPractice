import { e } from '../dom.js';
import { getAllIdeas } from '../api/data.js'; 

const section = document.getElementById('dashboard-holder');
section.remove();
section.addEventListener('click', onDetails);

let ctx = null;

export async function showCatalogPage(ctxTarget) {
    ctx = ctxTarget;
    ctx.showSection(section);
    loadIdeas();
}

async function loadIdeas() {
    const ideas = await getAllIdeas();
    const fragment = document.createDocumentFragment();

    if (ideas.length != 0) {
        ideas.map(createIdeaCard).forEach(i => fragment.append(i));
        section.replaceChildren(fragment);
    } else {
        section.innerHTML = '<h1>No ideas yet! Be the first one :)</h1>';
    }
    
}

function createIdeaCard(idea) {
    const element = e('div', { className: 'card overflow-hidden current-card details' });
    element.style.width = '20rem';
    element.style.height = '18rem';

    element.innerHTML = [
        '<div class="card-body">',
            `<p class="card-text">${idea.title}</p>`,
        '</div>',
        `<img class="card-image" src="${idea.img}" alt="Card image cap">`,
        `<a data-id="${idea._id}" class="btn" href="">Details</a>`
    ].join('');

    return element;
}

function onDetails(event) {
    event.preventDefault();

    if (event.target.tagName != 'A') {
        return;
    }

    const id = event.target.dataset.id;
    ctx.goTo('details', id);
}
