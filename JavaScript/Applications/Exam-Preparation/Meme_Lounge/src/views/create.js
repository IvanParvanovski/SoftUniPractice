import { createMeme } from '../api/data.js';
import { html } from '../lib.js';
import { notify } from '../notify.js';

// Create Meme Page ( Only for logged users )

const createTmp = (onSubmit) => html`
<section id="create-meme">
    <form id="create-form" @submit=${onSubmit}>
        <div class="container">
            <h1>Create Meme</h1>
            <label for="title">Title</label>
            <input id="title" type="text" placeholder="Enter Title" name="title">
            <label for="description">Description</label>
            <textarea id="description" placeholder="Enter Description" name="description"></textarea>
            <label for="imageUrl">Meme Image</label>
            <input id="imageUrl" type="text" placeholder="Enter meme ImageUrl" name="imageUrl">
            <input type="submit" class="registerbtn button" value="Create Meme">
        </div>
    </form>
</section>`;

export function createPage(ctx) {
    ctx.render(createTmp(onSubmit));

    async function onSubmit(event) {
        event.preventDefault();

        const form = event.target;
        const formData = new FormData(form);

        const title = formData.get('title').trim();
        const description = formData.get('description').trim();
        const imageUrl = formData.get('imageUrl').trim();
        
        try {
            if (title == '' || description == '' || imageUrl == '') {
                throw new Error('Please fill in all fields!');
            }
    
            await createMeme({ title, description, imageUrl });
            ctx.page.redirect('/catalog');
        } catch(err) {
            notify(err.message);
        }
        
    }
}
