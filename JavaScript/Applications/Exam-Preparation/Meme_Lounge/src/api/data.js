import * as api from './api.js';

export const login = api.login;
export const register = api.register;
export const logout = api.logout;

const endpoits = {
    all: '/data/memes?sortBy=_createdOn%20desc',
    create: '/data/memes',
    byId: (id) => `/data/memes/${id}`,
    edit: (id) => `/data/memes/${id}`,
    delete: (id) => `/data/memes/${id}`,
    profileMemes: (id) => `/data/memes?where=_ownerId%3D%22${id}%22&sortBy=_createdOn%20desc`,
};

export async function getAllMemes() {
    return api.get(endpoits.all);
}

export async function getMemeById(id) {
    return api.get(endpoits.byId(id));
}

export async function getProfileMemes(profileId) {
    return api.get(endpoits.profileMemes(profileId));
}

export async function createMeme(data) {
    return api.post(endpoits.create, data);
}

export async function editMeme(id, data) {
    return api.put(endpoits.edit(id), data);
}

export async function deleteMeme(id) {
    return api.del(endpoits.delete(id));
}
