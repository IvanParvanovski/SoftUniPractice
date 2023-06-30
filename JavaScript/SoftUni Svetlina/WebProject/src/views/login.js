import { html } from '../lib.js';
import { getUserData, setUserData, login } from '../util.js';

const loginTmp = (onSubmit) => html`
    <div class="wrapper">
    <form @submit=${onSubmit} class="primary-form">
        <h1 class="form-title">Login Form</h1>
        
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
        
        <button type="submit" class="submit-btn">Login</button>

        <p>
            <span>  If you don't have a profile click <a class="link --highlighted" href="/register">here</a></span>
        </p>
    </form>
    </div>
     
`;


export function loginPage(ctx) {
    const user = getUserData();
    if (user != undefined) {
        ctx.page.redirect('/');
    } else {
        ctx.render(loginTmp(onSubmit))
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
            await login(email, password);

            ctx.updateNav(true);
            ctx.page.redirect('/');
        } catch (err) {
            console.error(err);
        }

    }
}