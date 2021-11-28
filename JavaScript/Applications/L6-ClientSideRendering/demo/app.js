import { renderTemplate } from './engine.js';

async function start() {
    const data = await (await fetch('./data.json')).json();
    const template = await (await fetch('./article.html')).text();

    const main = document.querySelector('main');

    const articleTemplateEngine = renderTemplate(template);
    main.innerHTML = data.map(articleTemplateEngine).join('');
}

start();
