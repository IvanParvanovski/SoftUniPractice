import { html } from '../lib.js';
import { getAlbumById } from '../util.js';
import { editAlbum } from '../util.js';

const editTmp = (album, onSubmit) => html`
    <div class="wrapper">
    <form @submit=${onSubmit} class="primary-form --crud">
        <h1 class="form-title">Edit Form</h1>
        
        <div class="input-fields">
            <div class="field">
                <label for="name">Name</label>
                <i class="fa-solid fa-pen-nib"></i>
                <input id="name" name="name" type="text" value=${album.name}>
            </div>
    
            <div class="field">
                <label for="artist">Artist</label>
                <i class="fa-solid fa-circle-user"></i>
                <input id="artist" name="artist" type="text" value=${album.artist}>
            </div>
    
            <div class="field">
                <label for="genre">Genre</label>
                <i class="fa-solid fa-radio"></i>
                <input id="genre" name="genre" type="text" value=${album.genre}>
            </div>
    
            <div class="field">
                <label for="price">Price</label>
                <i class="fa-solid fa-tag"></i>
                <input id="price" name="price" type="text" value=${album.price}>
            </div>
        </div>

        <div class="input-fields">
            <div class="field">
                <label for="description">Description</label>

                <textarea name="description" id="description" cols="60" rows="8">${album.description}</textarea>
            </div>

            <div class="field">
                <label for="img">Img | Href </label>
                <i class="fa-solid fa-tag"></i>
                <input id="img" name="imgUrl" type="text" value="${album.imgUrl}">
            </div>

            <button type="submit" class="submit-btn">Submit</button>

        </div>
    </form>
    </div>
   
`;

export async function editPage(ctx) {
    const album = await getAlbumById(ctx.params.id);
    ctx.render(editTmp(album, onSubmit));


    async function onSubmit(event) {
        event.preventDefault();

        const form = event.target;
        const formData = new FormData(form);

        const name = formData.get('name');
        const imgUrl = formData.get('imgUrl');
        const price = formData.get('price');
        const artist = formData.get('artist');
        const genre = formData.get('genre');
        const description = formData.get('description');


        if (
            name.trim() == '' ||
            imgUrl.trim() == '' ||
            price.trim() == '' ||
            artist.trim() == '' ||
            genre.trim() == '' ||
            description.trim() == '') {

            return alert('Please fill in all input fields!');
        }


        await editAlbum(ctx.params.id, name, imgUrl, price, artist, genre, description);

        ctx.page.redirect(`/details/${ctx.params.id}`);
    }
}