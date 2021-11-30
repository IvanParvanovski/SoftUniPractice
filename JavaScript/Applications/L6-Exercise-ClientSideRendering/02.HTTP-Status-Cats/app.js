import { cats } from './catSeeder.js';
import { render } from './node_modules/lit-html/lit-html.js';
import listTemplateEngine from './templates/catList.js';

const catsSection = document.getElementById('allCats');
loadCats();

export function loadCats() {
    const result = listTemplateEngine(cats);
    render(result, catsSection);
}
