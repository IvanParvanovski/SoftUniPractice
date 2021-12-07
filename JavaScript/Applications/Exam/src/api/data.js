import * as api from './api.js';

export const login = api.login;
export const register = api.register;
export const logout = api.logout;

const endpoints = {
    all: '/data/albums?sortBy=_createdOn%20desc&distinct=name',
    create: '/data/albums',
    byId: (id) => `/data/albums/${id}`,
    edit: (id) => `/data/albums/${id}`,
    delete: (id) => `/data/albums/${id}`,
    albumByQuery: (query) => `/data/albums?where=name%20LIKE%20%22${query}%22`,
}

export async function getAll() {
    return api.get(endpoints.all);
}

export async function createAlbum(data) {
    return api.post(endpoints.create, data);
}

export async function getById(id) {
    return api.get(endpoints.byId(id));
}

export async function editAlbum(id, data) {
    return api.put(endpoints.edit(id), data);
}

export async function deleteAlbum(id) {
    return api.del(endpoints.delete(id));
}

export async function searchAlbum(query) {
    return api.get(endpoints.albumByQuery(query));
}
