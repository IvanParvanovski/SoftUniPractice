import { showView } from "./dom.js";

const registerSection = document.getElementById('form-sign-up');
registerSection.remove();

const registerForm = registerSection.querySelector('form');
registerForm.addEventListener('submit', onSubmit);


function onSubmit(event) {
    const formData = new FormData(registerForm);

    const email = formData.get('email');
    const password = formData.get('password');
    const repeatPassw
    ord = formData.get('repeatPassword');

}

export function showRegister() {
    showView(registerSection);
}
