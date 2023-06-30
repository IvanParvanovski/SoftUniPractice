const btnLoadBooks = document.getElementById('loadBooks');
btnLoadBooks.addEventListener('click', onLoad);

const titleInput = document.querySelector('input[name="title"]');
const authorInput = document.querySelector('input[name="author"]');
const formTitle = document.querySelector('form h3');
const btnSubmit = document.querySelector('form button');
btnSubmit.addEventListener('click', onSubmit);

let edditedBookId;
const tableBody = document.querySelector('table tbody');

async function onLoad() {
    const books = await (await fetch('http://localhost:3030/jsonstore/collections/books')).json();
    tableBody.innerHTML = '';
    
    for (const bookId in books) {
        const book = books[bookId];
        const tr = document.createElement('tr');

        tr.innerHTML = [
            `<td>${book.title}</td>`,
            `<td>${book.author}</td>`,
        ].join('');
        tr.setAttribute('book-id', bookId);

        const action = document.createElement('td');
        
        const btnEdit = document.createElement('button');
        btnEdit.addEventListener('click', onEdit);
        btnEdit.textContent = 'Edit';
        action.appendChild(btnEdit);

        const btnDelete = document.createElement('button');
        btnDelete.addEventListener('click', onDelete);
        btnDelete.textContent = 'Delete';
        action.appendChild(btnDelete);

        action.appendChild(btnDelete);
        tr.appendChild(action);
        tableBody.appendChild(tr);
    }
}

async function onEdit(event) {
    const tr = event.target.parentNode.parentNode;
    edditedBookId = tr.getAttribute('book-id');

    const book = await (await fetch('http://localhost:3030/jsonstore/collections/books/' + edditedBookId)).json();
    
    titleInput.value = book.title;
    authorInput.value = book.author;
    formTitle.textContent = 'Edit FORM';
    btnSubmit.textContent = 'Save';
}  

async function onSubmit(event) {
    event.preventDefault();

    if (edditedBookId != undefined) {
        const response = await fetch('http://localhost:3030/jsonstore/collections/books/' + edditedBookId, {
            method: 'put',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: titleInput.value, author: authorInput.value  }),
        });
        
       
        edditedBookId = undefined;
    } else {
        const title =  titleInput.value;
        const author = authorInput.value;

        if (title && author) {
            const response = await fetch('http://localhost:3030/jsonstore/collections/books/', {
                method: 'post',
                headers: {'Content-Type': 'application/json'}, 
                body: JSON.stringify({ title, author }),
            });

            console.log(response);
        }
    }

    titleInput.value = '';
    authorInput.value = '';
}

async function onDelete(event) {
    const row =  event.target.parentNode.parentNode;
    const rowId = row.getAttribute('book-id');

    row.remove();
    await fetch('http://localhost:3030/jsonstore/collections/books/' + rowId, {
        method: 'delete',
    });
}
