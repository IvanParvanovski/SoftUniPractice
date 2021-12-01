import { createIdea } from '../api/data.js';
import { html } from '../utilities.js';
import { loginPage } from './login.js';

const createTmp = () => html`
<div class="container home wrapper  my-md-5 pl-md-5">
    <div class=" d-md-flex flex-mb-equal ">
        <div class="col-md-6">
            <img class="responsive-ideas create" src="./images/creativity_painted_face.jpg" alt="">
        </div>
        <form class="form-idea col-md-5" method="post" @submit=${onSubmit}>
            <div class="text-center mb-4">
                <h1 class="h3 mb-3 font-weight-normal">Share Your Idea</h1>
            </div>
            <div class="form-label-group">
                <label for="ideaTitle">Title</label>
                <input type="text" id="ideaTitle" name="title" class="form-control" placeholder="What is your idea?"
                    required="" autofocus="">
            </div>
            <div class="form-label-group">
                <label for="ideaDescription">Description</label>
                <textarea type="text" name="description" class="form-control" placeholder="Description"
                    required=""></textarea>
            </div>
            <div class="form-label-group">
                <label for="inputURL">Add Image</label>
                <input type="text" id="inputURL" name="imageURL" class="form-control" placeholder="Image URL"
                    required="">
            </div>
            <button class="btn btn-lg btn-dark btn-block" type="submit">Create</button>

            <p class="mt-5 mb-3 text-muted text-center">© SoftTerest - 2021.</p>
        </form>
    </div>
</div>`;

export function createPage(ctx) {
    if (sessionStorage.getItem('userData') != null) {
        ctx.render(createTmp());
    } else {
        loginPage(ctx);
    }
}

async function onSubmit(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    
    const title = formData.get('title');
    const description = formData.get('description');
    const img = formData.get('imageURL');

    if (title < 6 || description < 10 || img < 5) {
        return;
    }

    await createIdea({ title, description, img });
    
    form.reset();
}
