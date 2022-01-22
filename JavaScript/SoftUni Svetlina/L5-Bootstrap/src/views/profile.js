import { html } from '../lib.js';

const profileTmp = (id) => html`
<h1>Profile Page ${id}</h1>`;

export function profilePage(ctx) {
    ctx.render(profileTmp(ctx.params.id))
}

