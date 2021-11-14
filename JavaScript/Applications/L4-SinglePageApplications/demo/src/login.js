import { showSection, request, showButtons } from './dom.js';

const loginSection = document.getElementById('loginSection');
loginSection.remove();

const form = loginSection.querySelector('form');
form.addEventListener('submit', onSubmit);

export function showLoginPage() {
    showSection(loginSection);
}

async function onSubmit(event) {
    event.preventDefault();

    const formData = new FormData(form);
    
    const email = formData.get('email').trim();
    const password = formData.get('password').trim();

    try {
        const user = await request('http://localhost:3030/users/login', {
            method: 'post',
            body: JSON.stringify({email, password}),
        });

        sessionStorage.setItem('token', user.accessToken);
        alert('Success!');
        showButtons();
        form.reset();
    } catch (error) {
        alert(error);
    }
}
