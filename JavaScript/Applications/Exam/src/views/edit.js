import { editAlbum, getById } from '../api/data.js';
import { html } from '../lib.js';

const editTmp = (album, onSubmit) => html`
<section class="editPage">
    <form @submit=${onSubmit}>
        <fieldset>
            <legend>Edit Album</legend>

            <div class="container">
                <label for="name" class="vhide">Album name</label>
                <input id="name" name="name" class="name" type="text" value="${album.name}">

                <label for="imgUrl" class="vhide">Image Url</label>
                <input id="imgUrl" name="imgUrl" class="imgUrl" type="text" value="${album.imgUrl}">

                <label for="price" class="vhide">Price</label>
                <input id="price" name="price" class="price" type="text" value="${album.price}">

                <label for="releaseDate" class="vhide">Release date</label>
                <input id="releaseDate" name="releaseDate" class="releaseDate" type="text" value="${album.releaseDate}">

                <label for="artist" class="vhide">Artist</label>
                <input id="artist" name="artist" class="artist" type="text" value="${album.artist}">

                <label for="genre" class="vhide">Genre</label>
                <input id="genre" name="genre" class="genre" type="text" value="${album.genre}">

                <label for="description" class="vhide">Description</label>
                <textarea name="description" class="description" rows="10"
                    cols="10">${album.description}</textarea>

                <button class="edit-album" type="submit">Edit Album</button>
            </div>
        </fieldset>
    </form>
</section>`;

export async function editPage(ctx) {
    const album = await getById(ctx.params.id);
    ctx.render(editTmp(album, onSubmit));

    async function onSubmit(event) {
        event.preventDefault();

        const form = event.target;
        const formData = new FormData(form);

        const name = formData.get('name').trim();
        const imgUrl = formData.get('imgUrl').trim();
        const price = formData.get('price').trim();
        const releaseDate = formData.get('releaseDate').trim();
        const artist =  formData.get('artist').trim();
        const genre = formData.get('genre').trim();
        const description = formData.get('description').trim();
        
        if (
            name == '' || 
            imgUrl == '' || 
            price == '' || 
            releaseDate == '' || 
            artist == '' || 
            genre == '' ||
             description == '') {

            return alert('Please fill in all input fields!');
        }

        album.name = name;
        album.imgUrl = imgUrl;
        album.price = price;
        album.releaseDate = releaseDate;
        album.artist = artist;
        album.genre = genre;
        album.description = description;
        
        await editAlbum(ctx.params.id, album);
        ctx.page.redirect(`/details/${ctx.params.id}`);
    }
}
