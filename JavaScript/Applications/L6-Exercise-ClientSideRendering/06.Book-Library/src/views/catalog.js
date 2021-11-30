import { html, until } from './lib.js';
import { getAllBooks } from '../api/data.js';
import { deleteBook } from '../api/data.js';
import { showUpdate } from './update.js';

const catalogTmp = (booksPromise) => html`
 <table>
    <thead>
        <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Action</th>
        </tr>
    </thead>
    <tbody>
        ${until(booksPromise(), html`<tr><td colSpan="3">Loading&hellip;</td></tr>`)}
    </tbody>
</table>`;

const bookRow = (book, onEdit, onDelete) => html`
<tr>
    <td>${book.author}</td>
    <td>${book.title}</td>
    <td>
        <button @click=${onEdit}>Edit</button>
        <button @click=${onDelete}>Delete</button>
    </td>
</tr>`;


export function showCatalog(ctx) {
    return catalogTmp(loadBooks());
}


async function loadBooks(onTrigger) {
    const books = await getAllBooks();
    return Object.values(books).map(b => bookRow(b, onEdit.bind(null, b, onEdit)));
}

function onEdit(book) {
}

async function onDelete(book) {
}

