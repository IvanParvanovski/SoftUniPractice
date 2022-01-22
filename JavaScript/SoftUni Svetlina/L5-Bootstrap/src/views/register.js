import { html } from '../lib.js';

const registerTmp = () => html`
<h1>Register Page</h1>`;

export function registerPage(ctx) {
    ctx.render(registerTmp())
}

