import { showHome } from '../app.js';
import { showLogin } from './login.js';
import { showRegister } from './register.js';

const views = {
    'homeLink': showHome,
    'loginLink': showLogin,
    'registerLink': showRegister,
    'logoutBtn': logoutUser
};

const mainContainer = document.getElementById('container');
const footerSection = document.querySelector('footer');

const navSection = document.querySelector('nav');
navSection.addEventListener('click', navigate);

function navigate(event) {
    const view = views[event.target.id];

    if (typeof view != 'function') { return; }

    event.preventDefault();
    view(event);
}

function updateNav() {
    const userData = sessionStorage.getItem('userData');
    const userLinks = navSection.querySelectorAll('.user');
    const guestLinks = navSection.querySelectorAll('.guest');

    if (userData != null) {
        userLinks.forEach(e => e.style.display = 'block');
        guestLinks.forEach(e => e.style.display = 'none');
        navSection.querySelector('#welcomeMsg').textContent = `Welcome, ${JSON.parse(userData).email}`;
    } else {
        userLinks.forEach(e => e.style.display = 'none');
        guestLinks.forEach(e => e.style.display = 'block');
    }
}


export function showView(section) {
    mainContainer.replaceChildren();

    mainContainer.appendChild(navSection);
    updateNav();

    mainContainer.appendChild(section);
    mainContainer.appendChild(footerSection);
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

async function logoutUser(event) {
    event.preventDefault();
    event.stopImmediatePropagation();

    const {_token} = JSON.parse(sessionStorage.getItem('userData'));

    await fetch('http://localhost:3030/users/logout', {
        headers: {
            'X-Authorization': _token,
        },
    });

    sessionStorage.removeItem('userData');

    showLogin();
}
