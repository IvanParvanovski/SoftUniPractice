import { html } from '../node_modules/lit-html/lit-html.js';
import catCard from './catCard.js';

const listTemplateEngine = (cats) => html`
<ul>
    ${cats.map(catCard)}
</ul>
`;


export default listTemplateEngine;
