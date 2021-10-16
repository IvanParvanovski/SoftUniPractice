function validate() {
    const emailInput = document.getElementById('email');
    emailInput.addEventListener('change', onChange);

    function onChange(event) {
        const regexPattern = /^\w+@\w+\.\w+$/;

        const emailElement = event.target;
        const emailValue = emailElement.value;

        const match = regexPattern.test(emailValue);
        if (match) {
            emailElement.classList.remove('error');
        } else {
            emailElement.classList.add('error');
        }
    }
}