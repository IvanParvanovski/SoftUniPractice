import { html, render } from './node_modules/lit-html/lit-html.js';

const container = document.getElementById('root');
const form = document.getElementById('townForm');
form.addEventListener('submit', onSubmit);

const townsTemplateEngine = (t) => html`<li>${t}</li>`;
const townsListTemplateEngine = (towns) => html`
<ul>
    ${towns.map(townsTemplateEngine)}
</ul>
`;

function onSubmit(event) {
    event.preventDefault();

    const formData = new FormData(form);
    const towns = formData.get('towns').split(',').map(t => t.trim());
    const result = townsListTemplateEngine(towns);

    render(result, container);
}
