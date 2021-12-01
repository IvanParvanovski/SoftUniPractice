const host = 'http://localhost:3030';

async function request(url, options) {
    try {
        const response = await fetch(host + url, options);

        if (response.ok == false) {
            if (response.status == 403) {
                sessionStorage.removeItem('userData');
            }

            const err = response.json();
            throw new Error(err.message);
        }
    
        if (response.status == 204) {
            return response;
        } 

        return response.json();
    } catch(err) {
        alert(err);
        throw err;
    }
}

function createOptions(method='get', data) {
    const options = {
        method,
        headers: {},
    }

    if (data != undefined) {
        options.headers['Content-Type'] = 'application/json';
        options.body = JSON.stringify(data);
    }
    
    const userData = sessionStorage.getItem('userData');
    if (userData != null) {
        options.headers['X-Authorization'] = JSON.parse(userData).token;
    }

    return options;
}

export async function get(url) {
    return request(url, createOptions());
}

export async function post(url, data) {
    return request(url, createOptions('post', data));
}

export async function put(url, data) {
    return request(url, createOptions('put', data));
}

export async function del(url) {
    return request(url, createOptions('delete'));
}

export async function login(email, password) {
    const result = await post('/users/login', {email, password});

    const userData = {
        email: result.email,
        id: result._id,
        token: result.accessToken,
    };

    setUserData(userData);
}

export async function register(email, password) {
    const result = await post('/users/register', {email, password});

    const userData = {
        email: result.email,
        id: result._id,
        token: result.accessToken,
    };

    setUserData(userData);
}

export async function logout() {
    await get('/users/logout');
    clearUserData();
}

export function getUserData() {
    return JSON.parse(sessionStorage.getItem('userData'));
}

export function setUserData(data) {
    sessionStorage.setItem('userData', JSON.stringify(data));
}

export function clearUserData() {
    sessionStorage.removeItem('userData');
}
   