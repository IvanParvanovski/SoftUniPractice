import { html } from '../lib.js';
import { register } from '../api/data.js';

const registerTmp = (onSubmit) => html`
<section id="registerPage">
    <form @submit=${onSubmit}>
        <fieldset>
            <legend>Register</legend>

            <label for="email" class="vhide">Email</label>
            <input id="email" class="email" name="email" type="text" placeholder="Email">

            <label for="password" class="vhide">Password</label>
            <input id="password" class="password" name="password" type="password" placeholder="Password">

            <label for="conf-pass" class="vhide">Confirm Password:</label>
            <input id="conf-pass" class="conf-pass" name="conf-pass" type="password" placeholder="Confirm Password">

            <button type="submit" class="register">Register</button>

            <p class="field">
                <span>If you already have profile click <a href="/login">here</a></span>
            </p>
        </fieldset>
    </form>
</section>`;

export function registerPage(ctx) {
    ctx.render(registerTmp(onSubmit));

    async function onSubmit(event) {
        event.preventDefault();

        const form = event.target;
        const formData = new FormData(form);

        const email = formData.get('email');
        const password = formData.get('password');
        const repeatPassword = formData.get('conf-pass');

        if (email == '' || password == '') {
            return alert('Please fill in all fields!');
        }

        if (password != repeatPassword) {
            return alert('Passwords do not match!');
        }

        const user = await register(email, password);
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
