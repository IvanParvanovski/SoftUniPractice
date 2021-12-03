import { register } from '../api/api.js';
import { html } from '../lib.js';

const registerTmp = (onSubmit, errorMsg) => html`
<div class="row space-top">
    <div class="col-md-12">
        <h1>Register New User</h1>
        <p>Please fill all fields.</p>
    </div>
</div>
<form @submit=${onSubmit}>
    <div class="row space-top">
        <div class="col-md-4">
            ${errorMsg ? html`<div class="error">${errorMsg}</div>` : null}
            <div class="form-group">
                <label class="form-control-label" for="email">Email</label>
                <input class="form-control ${errorMsg && errorMsg != 'Both passwords do not match!' ? 'is-invalid': ''}" id="email" type="text" name="email">
            </div>
            <div class="form-group">
                <label class="form-control-label" for="password">Password</label>
                <input class="form-control ${errorMsg ? 'is-invalid': ''}" id="password" type="password" name="password">
            </div>
            <div class="form-group">
                <label class="form-control-label" for="rePass">Repeat</label>
                <input class="form-control ${errorMsg ? 'is-invalid': ''}" id="rePass" type="password" name="rePass">
            </div>
            <input type="submit" class="btn btn-primary" value="Register" />
        </div>
    </div>
</form>`;


export function registerPage(ctx) {
    update();

    function update(errorMsg) {
        ctx.render(registerTmp(onSubmit, errorMsg))
    }

    async function onSubmit(event) {
        event.preventDefault();
    
        const form = event.target;
        const formData = new FormData(form);
    
        const email = formData.get('email');
        const passsword = formData.get('password');
        const repeatPassword = formData.get('rePass');
        
        try {
            if (passsword != repeatPassword) {
                throw new Error('Both passwords do not match!');
            }
            
            await register(email, passsword);   
            ctx.updateUserNav();
            ctx.page.redirect('/');
        } catch (err) {
            alert(err);
            update(err.message);
        }
    }
}
