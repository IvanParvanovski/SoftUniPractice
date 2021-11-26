import { showHome } from "../app.js";
import { showView } from "./dom.js";

const registerSection = document.getElementById('form-sign-up');
registerSection.remove();

const registerForm = registerSection.querySelector('form');
registerForm.addEventListener('submit', onSubmit);


async function onSubmit(event) {
    event.preventDefault();

    const formData = new FormData(registerForm);

    const email = formData.get('email');
    const password = formData.get('password');
    const repeatPassword = formData.get('repeatPassword');

    try {
        if (email == '' || password == '' || repeatPassword == '') {
            throw new Error('Please fill in all input fields!');
        } else if (password.length < 6) {
            throw new Error('The password is too short!');
        } else if (password != repeatPassword) {
            throw new Error('Both passwords do not match!');
        }

        const user = await registerUser({email, password});

        sessionStorage.setItem('userData', JSON.stringify({
            email: user.email,
            _id: user._id,
            _token: user.accessToken,
        }));
        
        registerForm.reset();
        showHome();
    } catch (err) {
        alert(err);
    }
}

async function registerUser(data) {
    const response = await fetch('http://localhost:3030/users/register', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (response.ok == false) {
        const error = response.json();
        throw new Error(error.message);
    }

    const user = await response.json();
    
    return user;
} 

export function showRegister() {
    showView(registerSection);
}
