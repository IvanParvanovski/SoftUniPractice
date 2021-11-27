import { register } from '../api/api.js';

const section = document.getElementById('registerPage');
section.remove();

const form = section.querySelector('form');
form.addEventListener('submit', onSubmit);

let ctx = null;

export async function showRegisterPage(ctxTarget) {
    ctx = ctxTarget;
    ctx.showSection(section);
}

export async function onSubmit(event) {
    event.preventDefault();

    const formData = new FormData(form);
    
    const email = formData.get('email').trim();
    const password = formData.get('password').trim();
    const rePass = formData.get('repeatPassword').trim();

    if (!email || !password) {
        return alert('All fields are required!');
    }
    
    if (password != rePass) {
        return alert('Passwords don\'t match!')
    }

    const regexPattern = /.{3,}/;
    const regex = new RegExp(regexPattern);

    if (!regex.test(email)) {
        return alert('The email is invalid!');
    }

    try {
        await register(email, password);
        form.reset();
    
        ctx.goTo('home');
        ctx.updateNav();
    } catch (err) {
        alert(err);
    }
}
