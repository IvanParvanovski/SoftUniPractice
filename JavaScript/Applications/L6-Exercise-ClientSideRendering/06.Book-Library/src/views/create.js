import { html } from './lib.js';
import { createBook } from '../api/data.js';

const createTmp = (onSuccess) => html`
<form @submit=${(ev) => onSubmit(ev, onSuccess)} id="add-form">
    <h3>Add book</h3>
    <label>TITLE</label>
    <input type="text" name="title" placeholder="Title...">
    <label>AUTHOR</label>
    <input type="text" name="author" placeholder="Author...">
    <input type="submit" value="Submit">
</form>`;

export function showCreate(ctx) {
    if (ctx.book != undefined) {
        return null;
    }
    
    return createTmp(ctx.update);
}

async function onSubmit(event, onSuccess) {
    event.preventDefault();
    
    const form = event.target;
    const formData = new FormData(form);

    const title = formData.get('title').trim();
    const author = formData.get('author').trim();

    await createBook({ title, author });

    form.reset();
    onSuccess();
}
