import * as api from './api.js';

export function getAllBooks() {
    return api.get('/jsonstore/collections/books');
}

export function getBookById(id) {
    return api.get(`/jsonstore/collections/books/${id}`);
}

export async function createBook(data) {
    return api.post('/jsonstore/collections/books/', data);
}

export function updateBook(id, data) {
    return api.put(`/jsonstore/collections/books/${id}`, data);
}

export function deleteBook(id) {
    return api.del(`/jsonstore/collections/books/${id}`);
}

