import { html } from "../lib.js";
import { createAlbum } from '../util.js'

const createTmp = (onSubmit, ctx) => html`
    <div class="wrapper">
    <form @submit=${(event) => onSubmit(event, ctx)} class="primary-form --crud">
        <h1 class="form-title">Create Form</h1>
        
        <div class="input-fields">
            <div class="field">
                <label for="name">Name</label>
                <i class="fa-solid fa-pen-nib"></i>
                <input placeholder="Inside out" name="name" id="name" type="text">
            </div>
    
            <div class="field">
                <label for="artist">Artist</label>
                <i class="fa-solid fa-circle-user"></i>
                <input placeholder="Erick Housman" name="artist" id="artist" type="text">
            </div>
    
            <div class="field">
                <label for="genre">Genre</label>
                <i class="fa-solid fa-radio"></i>
                <input placeholder="jazz" name="genre" id="genre"  type="text">
            </div>
    
            <div class="field">
                <label for="price">Price</label>
                <i class="fa-solid fa-tag"></i>
                <input id="price" type="text" name="price" placeholder="$25.12">
            </div>
        </div>

        <div class="input-fields">
            <div class="field">
                <label for="description">Description</label>

                <textarea name="descrtiption" id="description" cols="60" rows="8" placeholder="This is an insightful song about ardent secessionist"></textarea>
            </div>

            <div class="field">
                <label for="img">Img | Href </label>
                <i class="fa-solid fa-tag"></i>
                <input id="img" type="text" name="img" placeholder="https://images.unsplash.com/photo-1682542686319-393272073c6d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80">
            </div>

            <button type="submit" class="submit-btn">Submit</button>

        </div>
    </form>
    </div>
   
`;

export async function createPage(ctx) {
    ctx.render(createTmp(onSubmit, ctx));
}

async function onSubmit(event, ctx) {
    event.preventDefault();

    const formData = new FormData(event.target);

    const name = formData.get('name');
    const artist = formData.get('artist');
    const genre = formData.get('genre');
    const price = formData.get('price');
    const description = formData.get('descrtiption');
    const imgUrl = formData.get('img');


    if (
        name.trim() == '' ||
        imgUrl.trim() == '' ||
        price.trim() == '' ||
        artist.trim() == '' ||
        genre.trim() == '' ||
        description.trim() == '') {

        return alert('Please fill in all input fields!');
    }

    await createAlbum(name, imgUrl, price, artist, genre, description);
    ctx.page.redirect(`/catalogue`);
}