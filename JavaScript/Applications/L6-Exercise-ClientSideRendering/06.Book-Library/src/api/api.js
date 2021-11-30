const host = 'http://localhost:3030';

async function request(url, options) {
    try {
        const response = await fetch(host + url, options);
        
        if (response.ok == false) {
            throw new Error(`${response.status} ${response.statusText}`);
        }

        if (response.status == 204) {
            return response;
        }

        return response.json();
    } catch (err) {
        alert(err);
        throw err;
    }
}

function createOptions(method='get', data) {
    const options = {
        method,
        headers: {}
    };

    if (data != undefined) {
        options.headers['Content-Type'] = 'application/json';
        options.body = JSON.stringify(data);
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
