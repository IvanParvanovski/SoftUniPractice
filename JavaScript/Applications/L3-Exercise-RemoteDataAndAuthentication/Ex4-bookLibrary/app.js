const tbody = document.querySelector('tbody');
const createForm = document.getElementById('createForm');
const editForm = document.getElementById('editForm');

document.getElementById('loadBooks').addEventListener('click', loadBooks);

createForm.addEventListener('submit', onCreate);
editForm.addEventListener('submit', onEditSubmit);

tbody.addEventListener('click', onTableClick);

loadBooks();

async function onEditSubmit(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    
    const id = formData.get('id');
    const title = formData.get('title');
    const author = formData.get('author');

    const book = await updateBook(    
        id, {title, author}
    );
    
    form.reset();
    createForm.style.display = 'block';
    editForm.style.display = 'none';
    loadBooks();
}

function onTableClick(event) {
    if (event.target.className == 'delete') {
        onDelete(event.target);
    } else if (event.target.className == 'edit') {
        onEdit(event.target);
    }
}

async function onDelete(button) {
    const id = button.parentElement.dataset.id;

    await deleteBook(id);
    button.parentElement.parentElement.remove();
}

async function onEdit(button) {
    const id = button.parentElement.dataset.id;
    const book = await loadBookById(id);

    createForm.style.display = 'none';
    editForm.style.display = 'block';

    editForm.querySelector('[name="id"]').value = book._id;
    editForm.querySelector('[name="author"]').value = book.author;
    editForm.querySelector('[name="title"]').value = book.title;

}

async function onCreate(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    const book = await createBook({
        title: formData.get('title'),
        author: formData.get('author'),
    });

    const row = createRow(book._id, book);
    tbody.appendChild(row);
    form.reset();
}

async function request(url, options) {
    const response = await fetch(url, options);
    if (options && options.body != undefined) {
        Object.assign(options, {
            headers: {
                'Content-Type': 'application/json',
            },
        });
    }

    if (response.ok != true) {
        const error = await response.json();
        alert(error.message);
        throw new Error(error.message);
    }

    const data = response.json();
    return data;
}

async function createBook(data) {
    const record = {
        method: 'post',
        body: JSON.stringify(data),
    };

    return await request(
        'http://localhost:3030/jsonstore/collections/books',
        record
    );
}

async function deleteBook(id) {
    return await request('http://localhost:3030/jsonstore/collections/books/' + id, {
        method: 'delete'
    });
}

async function updateBook(id, book) {
    return await request('http://localhost:3030/jsonstore/collections/books/' + id, {
        method: 'put',
        body: JSON.stringify(book),
    });
}

function createRow(id, book) {
    const row = document.createElement('tr');
    row.innerHTML = [
        '<tr>',
        `<td>${book.title}</td>`,
        `<td>${book.author}</td>`,
        `<td data-id=${id}>`,
            '<button class="edit">Edit</button>',
            '<button class="delete">Delete</button>',
        '</td>',
        '</tr>',
    ].join('');

    return row;
}

async function loadBooks() {
    const books = await request('http://localhost:3030/jsonstore/collections/books');
    tbody.replaceChildren(
        ...Object
            .entries(books)
            .map(([id, book]) => createRow(id, book)));
}

async function loadBookById(id) {
    const url = 'http://localhost:3030/jsonstore/collections/books/' + id
    return request(url);
}
