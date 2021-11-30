import { html, render } from './node_modules/lit-html/lit-html.js';
import { towns } from './towns.js';

const townItem = (town, active) => html`<li class=${active ? 'active' : ''}>${town}</li>`;
const townsListTmp = (towns, st) => html`<ul>${towns.map(t => townItem(t, t.toLowerCase().includes(st.toLowerCase())))}</ul>`;

const townsContainer = document.getElementById('towns');
const searchBtn = document.querySelector('button');
searchBtn.addEventListener('click', search);

render(townsList(towns, '(*invalid*)'), townsContainer);

function search() {
   const searchedText = document.getElementById('searchText').value;
   render(townsListTmp(towns, searchedText), townsContainer);
}


   