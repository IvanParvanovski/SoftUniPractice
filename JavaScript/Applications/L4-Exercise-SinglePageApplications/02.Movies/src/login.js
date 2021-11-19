import { showHome } from "../app.js";
import { showView } from "./dom.js";

const loginSection = document.getElementById('form-login');
loginSection.remove();

const loginForm = loginSection.querySelector('form');
loginForm.addEventListener('submit', onSubmit);

async function onSubmit(event) {
    event.preventDefault();

    const formData = new FormData(loginForm);

    const email = formData.get('email').trim();
    const password = formData.get('password').trim();

    try {
        if (email == '' || password == '') {
            throw new Error('Please fill in all input fields!');
        }
    
        const user = await loginUser({email, password});
        sessionStorage.setItem('userData', JSON.stringify({
            email: user.email,
            _id: user._id,
            _token: user.accessToken,
        }));

        loginForm.reset();
        showHome();
    } catch (err) {
        alert(err);
    }    
}

async function loginUser(data) {
    const response = await fetch('http://localhost:3030/users/login/', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (response.status == 403) {
        throw new Error('The email or password is incorrect!');
    } else if (response.ok == false) {
        const error = response.json();

        throw new Error(error.message);
    }

    const user = await response.json();
    return user;
}

export function showLogin() {
    showView(loginSection);
}
