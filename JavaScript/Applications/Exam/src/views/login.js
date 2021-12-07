import { login } from '../api/api.js';
import { html } from '../lib.js';
import { setUserData } from '../util.js';

const loginTmp = (onSubmit) => html`
<section id="loginPage">
    <form @submit=${onSubmit}>
        <fieldset>
            <legend>Login</legend>

            <label for="email" class="vhide">Email</label>
            <input id="email" class="email" name="email" type="text" placeholder="Email">

            <label for="password" class="vhide">Password</label>
            <input id="password" class="password" name="password" type="password" placeholder="Password">

            <button type="submit" class="login">Login</button>

            <p class="field">
                <span>If you don't have profile click <a href="/register">here</a></span>
            </p>
        </fieldset>
    </form>
</section>`;

export function loginPage(ctx) {
    ctx.render(loginTmp(onSubmit));

    async function onSubmit(event) {
        event.preventDefault();

        const form = event.target;
        const formData = new FormData(form);

        const email = formData.get('email');
        const password = formData.get('password');
        
        if (email == '' || password == '') {
            return alert('Please fill in all fields!');
        }

        const user = await login(email, password);
        const userData = {
            email: user.email,
            id: user._id,
            token: user.accessToken,
        };

        setUserData(userData);
        ctx.updateNav();
        ctx.page.redirect('/');
    }
}

