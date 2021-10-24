function validate() {
    const emailRegex = /^\w+@\w+\.\w+$/;

    const emailInput = document.getElementById('email');
    emailInput.addEventListener('change', onChange);

    function onChange(event) {
        const match = event.target.value.match(emailRegex);
        
        if (match == null) {
            emailInput.classList.add('error');
        } else {
            emailInput.classList.remove('error');
        }
    }
}