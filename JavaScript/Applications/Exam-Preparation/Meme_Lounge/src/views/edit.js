import { editMeme, getMemeById } from '../api/data.js';
import { html } from '../lib.js';
import { notify } from '../notify.js';
import { getUserData } from '../util.js';

// Edit Meme Page ( Only for logged user and creator to this meme )

const editTmp = (meme, onEdit) => html`
<section id="edit-meme">
    <form id="edit-form" @submit=${(ev) => onEdit(ev, meme)}>
        <h1>Edit Meme</h1>
        <div class="container">
            <label for="title">Title</label>
            <input id="title" type="text" placeholder="Enter Title" name="title" .value=${meme.title}>
            <label for="description">Description</label>
            <textarea id="description" placeholder="Enter Description" name="description" .value=${meme.description}></textarea>
            <label for="imageUrl">Image Url</label>
            <input id="imageUrl" type="text" placeholder="Enter Meme ImageUrl" name="imageUrl" .value=${meme.imageUrl}>
            <input type="submit" class="registerbtn button" value="Edit Meme">
        </div>
    </form>
</section>`;

export async function editPage(ctx) {
    const meme = await loadMeme();
    ctx.render(editTmp(meme, onEdit));

    function loadMeme() {
        const userData = getUserData();
        if (userData == null) {
            ctx.redirect('/login');
        }
    
        return getMemeById(ctx.params.id);
    }

    async function onEdit(event, meme) {
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
    
            meme.title = title;
            meme.description = description;
            meme.imageUrl = imageUrl;
    
    
            await editMeme(meme._id, meme);
            ctx.page.redirect(`/details/${meme._id}`);
        } catch(err) {
            notify(err.message);
        }
        
    }
}

