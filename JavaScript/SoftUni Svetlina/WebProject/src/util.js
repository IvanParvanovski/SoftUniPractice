// Configs

const host = 'http://localhost:3030'

const authEndPoints = {
    login: '/users/login',
    register: '/users/register',
    logout: '/users/logout',
}


export function getUserData() {
    return JSON.parse(sessionStorage.getItem('userData'));
}


export function clearUserData() {
    sessionStorage.removeItem('userData');
}


export function setUserData(data) {
    console.log(data);
    sessionStorage.setItem('userData', JSON.stringify(data));
}

const endpoints = {
    all: '/data/albums?sortBy=_createdOn%20desc&distinct=name',
    create: '/data/albums',
    byId: (id) => `/data/albums/${id}`,
    edit: (id) => `/data/albums/${id}`,
    delete: (id) => `/data/albums/${id}`,
    albumByQuery: (query) => `/data/albums?where=name%20LIKE%20%22${query}%22`,
};

// Requests

export async function getAllAlbums() {
    return await fetch(
        host + endpoints.all, {
        headers: { 'Content-Type': 'application/json' },
    }
    ).then((response) => response.json())
}

export async function createAlbum(
    name,
    imgUrl,
    price,
    artist,
    genre,
    description,
) {
    const userData = JSON.parse(sessionStorage.getItem('userData'));
    const releaseDateObj = new Date();
    const releaseDate = `${releaseDateObj.getDate()}:${releaseDateObj.getMonth()}:${releaseDateObj.getFullYear()}`;

    return await fetch(
        host + endpoints.create, {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
            'X-Authorization': userData.token,
        },
        body: JSON.stringify({ name, imgUrl, price, releaseDate, artist, genre, description })
    }
    )
}

export async function getAlbumById(id) {
    const response = await fetch(
        host + endpoints.byId(id), {
        method: 'get',
        headers: { 'Content-Type': 'application/json' }
    }
    );

    return await response.json();
}

export async function searchAlbums(query) {
    const response = await fetch(host + endpoints.albumByQuery(query));
    const songs = await response.json();

    return songs
}

export async function editAlbum(id,
    name,
    imgUrl,
    price,
    artist,
    genre,
    description
) {
    const userData = JSON.parse(sessionStorage.getItem('userData'));
    const releaseDateObj = new Date();
    const releaseDate = `${releaseDateObj.getDate()} - ${releaseDateObj.getMonth()} - ${releaseDateObj.getFullYear()}`;

    return await fetch(host + endpoints.edit(id), {
        method: 'put',
        body: JSON.stringify({ name, imgUrl, price, releaseDate, artist, genre, description }),
        headers: {
            'Content-Type': 'application/json',
            'X-Authorization': userData.token,
        }
    });
}

export async function deleteAlbum(id) {
    const userData = JSON.parse(sessionStorage.getItem('userData'));

    const response = await fetch(
        host + endpoints.delete(id), {
        method: 'delete',
        headers: {
            'X-Authorization': userData.token,
        }
    }
    )

    console.log(await response.json());
}

// Authentication

export async function login(email, password) {
    try {
        const response = await fetch(
            host + authEndPoints.login, {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        }
        )

        if (response.ok == false) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const result = await response.json();

        const userData = {
            email: result.email,
            id: result._id,
            token: result.accessToken,
        };

        setUserData(userData);

        return response;
    } catch (err) {
        throw err;
    }

}

export async function register(email, password) {
    try {
        const response = await fetch(
            host + authEndPoints.register, {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password }),
        }
        )

        if (response.ok == false) {
            const error = response.json();
            throw new Error(error.message);
        }

        const result = await response.json();

        const userData = {
            email: result.email,
            id: result._id,
            token: result.accessToken,
        };

        setUserData(userData);

        return response;
    } catch (err) {
        throw err;
    }


}

export async function logout() {
    await fetch(host + authEndPoints.logout)
    clearUserData();
}

