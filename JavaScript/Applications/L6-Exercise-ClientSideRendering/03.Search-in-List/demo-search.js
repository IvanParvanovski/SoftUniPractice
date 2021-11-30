import { html, render } from './node_modules/lit-html/lit-html.js';
import { towns as townNames } from './towns.js';

const townItemTmp = (town) => html`<li class=${town.match ? 'active' : ''}>${town.name}</li>`;
const townsListTmp = (towns) => html`<ul>${towns.map(townItemTmp)}</ul>`;

const towns = townNames.map(t => ({ name: t, match: false }));
const townsContainer = document.getElementById('towns');

const searchBtn = document.querySelector('button');
searchBtn.addEventListener('click', search);

update();

function update() {
    render(townsListTmp(towns), townsContainer);
}

function search() {
    const searchedText = document.getElementById('searchText').value.trim();

    let matches = 0;
    for (const town of towns) {
        if (town.name.toLowerCase().includes(searchedText.toLowerCase())) {
            town.match = true;
            matches++;
        } else {
            town.match = false;
        }
    }

    document.getElementById('result').textContent = `${matches} matches found`
    update();
}
