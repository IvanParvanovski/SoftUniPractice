const host = 'http://localhost:3030';

async function request(url, options) {
    try {
        const response = await fetch(host + url, options);
        
        if (response.ok == false) {
            if (response.status == 403) {
                sessionStorage.removeItem('userData');
            } 
            
            const error = response.json();
            throw new Error(error.message);
        }

        if (response.status == 204) {
            return response.json();
        } else { 
            return response;
        }

    } catch (err) {
        alert(err);
        throw err;
    }
}

async function createOptions(method = 'get', data) {
    const options = {
        method,
        headers: {}
    };

    if (data != undefined) {
        options.headers['Content-Type'] = 'application/json'
        options.body = JSON.stringify(data);
    }

    const userData = JSON.parse(sessionStorage.getItem('userData'));
    if (userData != null) {
        options.headers['X-Authorization'] = userData.token;
    }

    return options;
} 

export async function get(url) {
    return request(url);
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

export async function login(url, data) {
    const response = await request(url, createOptions('post', data));
    const userData = {
        email: response.email,
        id: response._id,
        token: response.accessToken,
    };

    sessionStorage.setItem('userData', JSON.stringify(userData));
}z

export async function register(url, data) {

}

export async function logout() {

}
