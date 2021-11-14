const main = document.querySelector('main');
const nav = document.querySelector('nav'); 

const guestBtns = nav.querySelector('#guest');
const userBtns = nav.querySelector('#user');

export function showSection(section) {
    main.replaceChildren(section);
}

export async function request(url, options) {
    if (options && options.method == 'post') {
        if (options.hasOwnProperty('headers')) {
            Object.assign(options.headers, {
                'Content-Type': 'application/json',
            })
        } else {
            Object.assign(options, {
                headers: {'Content-Type': 'application/json',
            }})
        }
    }

    const response = await fetch(url, options);

    if (response.ok == false) {
        throw new Error(`${response.status} ${response.statusText}`);
    }

    const result = await response.json();
    return result;
}

export function e(type, attributes, ...content) {
    const result = document.createElement(type);

    for (let [attr, value] of Object.entries(attributes || {})) {
        if (attr.substring(0, 2) == 'on') {
            result.addEventListener(attr.substring(2).toLocaleLowerCase(), value);
        } else {
            result[attr] = value;
        }
    }

    content = content.reduce((a, c) => a.concat(Array.isArray(c) ? c : [c]), []);

    content.forEach(e => {
        if (typeof e == 'string' || typeof e == 'number') {
            const node = document.createTextNode(e);
            result.appendChild(node);
        } else {
            result.appendChild(e);
        }
    });

    return result;
}

export function showButtons() {
    if (sessionStorage.token == null) {
        guestBtns.style.display = 'inline-block';
        userBtns.style.display = 'none';
    } else {
        guestBtns.style.display = 'none';
        userBtns.style.display = 'inline-block';
    }
}