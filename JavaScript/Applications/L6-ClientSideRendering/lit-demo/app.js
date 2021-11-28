import { render } from './node_modules/lit-html/lit-html.js'
import articleTemplate from './templates/article.js';

async function start() {
    const data = await (await fetch('./data.json')).json();
    const main = document.querySelector('main');
    const renderBtn = document.getElementById('renderBtn');
    renderBtn.addEventListener('click', onRender);

    function onRender() {
        const result = data.map(a => articleTemplate(onSubmit.bind(null, a), a));
        render(result, main);
   
    }

    function onSubmit(article, event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const content = formData.get('comment');

        article.comments.push({ content });
    }
}

start();
