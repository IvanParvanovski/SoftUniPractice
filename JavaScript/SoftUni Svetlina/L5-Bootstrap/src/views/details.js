import { html } from '../lib.js';

const detailsTmp = (id) => html`
<h1>Details Page ${id}</h1>
<h1>Details Page ${id}</h1>
<h1>Details Page ${id}</h1>
<h1>Details Page ${id}</h1>
<h1>Details Page ${id}</h1>
`;

export function detailsPage(ctx) {
    ctx.render(detailsTmp(ctx.params.id))
}

