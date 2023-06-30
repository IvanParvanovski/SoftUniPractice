async function solution() {
    const mainSection = document.getElementById('main');
    const articles = await getArticles();

    for (const articleConfig of articles) {
        const article = await (await fetch('http://localhost:3030/jsonstore/advanced/articles/details/' + articleConfig._id)).json();

        const accordion = document.createElement('div');
        accordion.className = 'accordion';

        const accordionHead = document.createElement('div');
        accordionHead.className = 'head';

        const accordionExtra = document.createElement('div');
        accordionExtra.className = 'extra';

        accordionHead.innerHTML = [
            `<span>${article.title}</span>`,
            `<button class="button" id="${article._id}">More</button>`
        ].join('');

        accordionHead.children[1].addEventListener('click', onClick); 
        accordionExtra.innerHTML = `<p>${article.content}</p>`
        
        accordion.appendChild(accordionHead);
        accordion.appendChild(accordionExtra);

        mainSection.appendChild(accordion);
    }

    function onClick(event) {
        if (event.target.innerHTML == 'Less') {
            event.target.innerHTML = 'More'
            event.target.parentNode.parentNode.children[1].style.display = 'none';
        } else if (event.target.innerHTML == 'More') {
            event.target.innerHTML ='Less';
            event.target.parentNode.parentNode.children[1].style.display = 'block';
        }
    }

    async function getArticles() {
        try {
            const url = 'http://localhost:3030/jsonstore/advanced/articles/list';
            const response = await fetch(url);
            
            if (response.status != 200) {
                throw new Error('Invalid HTTP Request!');
            }
            
            const data = await response.json();
            return data;
        } catch (error) {
            console.error(error);
        }
    }
}
