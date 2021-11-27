import { createIdea } from '../api/data.js';

const section = document.getElementById('createPage');
section.remove();

const form = section.querySelector('form');
form.addEventListener('submit', addIdea);

let ctx = null;

export async function showCreatePage(ctxTarget) {
    ctx = ctxTarget;
    ctx.showSection(section);
}

async function addIdea(event) {
    event.preventDefault();

    const formData = new FormData(form);

    const title = formData.get('title').trim();
    const description = formData.get('description').trim();
    const imgUrl = formData.get('imageURL').trim();

    if (title.length < 6) {
        return alert('The title is too short!')
    }

    if (description.length < 10) {
        return alert('The description is too short!');
    }

    if (imgUrl.length < 5) {
        return alert('The Image Url is too short!')
    }

    try {
        await createIdea({
            title,
            description,
            img: imgUrl
        });

        form.reset();
        ctx.goTo('catalog');
        ctx.updateNav();
    } catch (err) {
        alert(err)
    }
}
