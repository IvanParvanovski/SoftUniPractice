import { showSection, showButtons } from './dom.js';
import { login } from './api/data.js';

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

    await login('/users/login/', {email, password});

    alert('Success!');
    showButtons();
    form.reset();
}
