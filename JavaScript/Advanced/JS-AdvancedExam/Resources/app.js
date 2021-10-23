window.addEventListener('load', solve);

function solve() {
    const allHitsElement = document.querySelector('#all-hits .all-hits-container');
    const savedHitsElement = document.querySelector('#saved-hits .saved-container');
    const totalLikesElement = document.querySelector('#total-likes .likes');

    const inputElements = {
        genre: document.getElementById('genre'),
        name: document.getElementById('name'),
        author: document.getElementById('author'),
        date: document.getElementById('date'),
    }

    const addBtn = document.getElementById('add-btn');
    addBtn.addEventListener('click', addSong);

    function addSong(event) {
        event.preventDefault();
        
        let hasEmpty = false;
        for (const prop of Object.values(inputElements)) {
            if (prop.value == '') {
                hasEmpty = true;
                break;
            }
        }

        if (hasEmpty) {
            return;
        }

        const newDivElement = document.createElement('div');
        newDivElement.classList.add('hits-info');

        const imgElement = document.createElement('img');
        imgElement.src = './static/img/img.png';

        const genreElement = document.createElement('h2');
        genreElement.textContent = `Genre: ${inputElements.genre.value}`;

        const nameElement = document.createElement('h2');
        nameElement.textContent = `Name: ${inputElements.name.value}`;

        const authorElement = document.createElement('h2');
        authorElement.textContent = `Author: ${inputElements.author.value}`;

        const dateElement = document.createElement('h3');
        dateElement.textContent = `Date: ${inputElements.date.value}`;

        const saveBtn = document.createElement('button');
        saveBtn.textContent = 'Save song';
        saveBtn.classList.add('save-btn');

        const likeBtn = document.createElement('button');
        likeBtn.textContent = 'Like song';
        likeBtn.classList.add('like-btn');

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.classList.add('delete-btn');

        newDivElement.appendChild(imgElement);
        newDivElement.appendChild(genreElement);
        newDivElement.appendChild(nameElement);
        newDivElement.appendChild(authorElement);
        newDivElement.appendChild(dateElement);
        newDivElement.appendChild(saveBtn);
        newDivElement.appendChild(likeBtn);
        newDivElement.appendChild(deleteBtn);

        for (const prop of Object.values(inputElements)) {
            prop.value = '';
        }

        newDivElement.querySelector('.like-btn').addEventListener('click', likeSong);
        newDivElement.querySelector('.save-btn').addEventListener('click', saveSong);
        newDivElement.querySelector('.delete-btn').addEventListener('click', deleteSong);
        allHitsElement.appendChild(newDivElement);
    }

    function likeSong(event) {
        const paragraph = totalLikesElement.getElementsByTagName('p')[0];
        const text = paragraph.textContent;

        const splittedText = text.split(' ');
        const totalLikes = Number(splittedText[2]);

        paragraph.textContent = `Total Likes: ${totalLikes + 1}`;

        event.target.backgroundColor = 'gray';
        event.target.disabled = true;
    }

    function saveSong(event) {
        const parentDiv = event.target.parentElement;
        
        parentDiv.removeChild(parentDiv.querySelector('.like-btn'));
        parentDiv.removeChild(event.target);
        
        savedHitsElement.appendChild(parentDiv);
    }

    function deleteSong(event) {
        const parentDivElement = event.target.parentElement;
        const sectionElement = parentDivElement.parentElement;
        sectionElement.removeChild(parentDivElement);
    }
}

