import { html } from './lib.js';
import { updateBook } from '../api/data.js';

const updateTmp = (book, onSuccess) => html`
<form @submit=${(ev) => onSubmit(ev, onSuccess)} id="edit-form">
    <input type="hidden" name="id" .value=${book._id}>
    <h3>Edit book</h3>
    <label>TITLE</label>
    <input type="text" name="title" placeholder="Title..." .value=${book.title}>
    <label>AUTHOR</label>
    <input type="text" name="author" placeholder="Author..." .value=${book.author}>
    <input type="submit" value="Save">
</form>`; 

export function showUpdate(ctx) {
    if (ctx.book == undefined) {
        return null;
    }
    
    return updateTmp(ctx.book, ctx.updateTmp);
}

async function onSubmit(event, onSuccess) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    
    const id = formData.get('id');
    const title = formData.get('title').trim();
    const author = formData.get('author').trim();

    await updateBook(id, { title, author });

    form.reset();
    onSuccess();
}
