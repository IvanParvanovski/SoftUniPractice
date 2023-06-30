import { html } from '../lib.js';
import { setUserData, getUserData, login, register } from '../util.js';

const registerTmp = (onSubmit) => html`
    <div class="wrapper">
    <form @submit=${onSubmit} class="primary-form">
        <h1 class="form-title">Register Form</h1>
        
        <div class="field">
            <label for="email">Email</label>
            <i class="fa-solid fa-envelope"></i>
            <input id="email" name="email" placeholder="user@gmail.com" type="text">
        </div>
        <div class="field">
            <label for="password">Password</label>
            <i class="fa-solid fa-lock"></i>
            <input id="password" name="password" placeholder="********" type="password">
        </div>
        
        <button type="submit" class="submit-btn">Register</button>

        <p>
            <span>  If you have a profile click <a class="link --highlighted" href="/login">here</a></span>
        </p>
    </form>
    </div>

`;


export function registerPage(ctx) {
    const user = getUserData();
    if (user != undefined) {
        ctx.page.redirect('/');
    } else {
        ctx.render(registerTmp(onSubmit));
    }

    async function onSubmit(event) {
        event.preventDefault();

        const form = event.target;
        const formData = new FormData(form);

        const email = formData.get('email');
        const password = formData.get('password');

        if (email == '' || password == '') {
            return alert('Please fill in all fields!');
        }

        try {
            await register(email, password);

            ctx.updateNav(true);
            ctx.page.redirect('/');
        } catch (err) {
            console.error(err);
        }

    }
}