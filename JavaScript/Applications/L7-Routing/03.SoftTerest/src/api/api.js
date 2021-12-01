const host = 'http://localhost:3030';

async function request(url, options) {
    try {
        const response = await fetch(host + url, options);
        
        if (response.ok == false) {
            if (response.status == 401) {
                throw new Error('You are not authorized!');
            }

            throw new Error(`${response.status} ${response.statusText}`);
        }
        
        if (response == 204) {
            return response;
        } else {
            return response.json();
        }
    } catch (err) {
        alert(err);
    }
}

function createOptions(method='get', data) {
    const options = {
        method,
        headers: {},
    };

    if (data != undefined) {
        options.headers['Content-Type'] = 'application/json';
        options.body = JSON.stringify(data);
    }

    const userData = sessionStorage.getItem('userData');
    if (userData != null) {
        options.headers['X-Authorization'] = JSON.parse(userData).accessToken;
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

export async function login(data) {
    return request('/users/login', createOptions('post', data));
}

export async function register(data) {
    return request('/users/register', createOptions('post', data));
}

export async function logout() {
    sessionStorage.getItem('userData');

    if (userData != null) {
        const id = JSON.parse(userData)._id;
        await get(`/users/${id}`);
        sessionStorage.removeItem('userData');
    }
}
