import { request, showSection, showButtons } from './dom.js';

const registerSection = document.getElementById('registerSection');
registerSection.remove();

const form = registerSection.querySelector('form');
form.addEventListener('submit', onSubmit);

export function showRegisterPage() {
    showSection(registerSection);
}

async function onSubmit(event) {
    event.preventDefault();

    const formData = new FormData(form);

    const email = formData.get('email').trim();
    const password = formData.get('password').trim();
    const repeatedPassword = formData.get('rePass').trim();

    try {
        if (password != repeatedPassword) {
            throw new Error('Passwords don\'t match!');
        }

        const user = await request('http://localhost:3030/users/register', {
                method: 'post',
                body: JSON.stringify({email, password}),
        });

        sessionStorage.setItem('token', user.accessToken);
        alert('Success!');
        showButtons();
        form.reset();
    } catch (err) {
        alert(err);
    }
}
