import { html } from '../node_modules/lit-html/lit-html.js'

const commentTemplate = (comment) => html`<li>${comment.content}</li>`

export default commentTemplate;
