function solve() {
    const authorField = document.getElementById('creator');
    const titleField = document.getElementById('title');
    const contentField = document.getElementById('content');
    const publicationsSection = document.querySelector('main section');

    const createBtn = document.getElementsByClassName('create')[0];
    createBtn.addEventListener('click', (ev) => onClick(ev));

    function onDelete(event) {
        console.log(event.target.parentElement.parentElement.remove());
    }

    function onClick(event) {
        event.preventDefault();

        const author = authorField.value;
        const title = titleField.value;
        const content = contentField.value;

        const article = document.createElement('article');
        
        const articleHeading = document.createElement('h1');
        articleHeading.innerHTML = title;

        const articleAuthor = document.createElement('p');
        articleAuthor.innerHTML = 'Creator: ' + author;

        const articleContent = document.createElement('p');
        articleContent.innerHTML = content;

        const buttonsDiv = document.createElement('div');
        buttonsDiv.className = 'buttons'

        const deleteBtn = document.createElement('button');
        deleteBtn.classList.add('btn');
        deleteBtn.classList.add('delete');
        deleteBtn.innerHTML = 'Delete';
        deleteBtn.addEventListener('click', (ev) => onDelete(ev));

        buttonsDiv.appendChild(deleteBtn);


        article.appendChild(articleHeading);
        article.appendChild(articleAuthor)
        article.appendChild(articleContent);
        article.appendChild(buttonsDiv);

        publicationsSection.appendChild(article);
    }
}