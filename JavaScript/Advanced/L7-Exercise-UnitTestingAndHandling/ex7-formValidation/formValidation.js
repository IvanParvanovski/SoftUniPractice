function validate() {
    const regexPatterns = {
        username: /^[\d\w]{3,20}$/,
        password: /^+[\w]{5,15}$/,
        email: /^\w+@\w+\.\w+$/,
    };

    const inputElements = {
        username: document.getElementById('username'),
        email: document.getElementById('email'),
        password: document.getElementById('password'),
        confirmPassword: document.getElementById('confirm-password'),
    }

    const companyInfoElement = document.getElementById('companyInfo');
    const resultDivElement = document.getElementById('valid');

    const companyCheckboxElement = document.getElementById('company');
    companyCheckboxElement.addEventListener('change', onCheck);
    
    const submitButton = document.getElementById('submit');
    submitButton.addEventListener('click', submitData);

    function onCheck(event) {
        if (event.target.checked) {
            companyInfoElement.style.display = 'block';
            inputElements.companyNumber = document.getElementById('companyNumber');
        } else {
            companyInfoElement.style.display = 'none';
            delete inputElements.companyNumber;
        }
        console.log(inputElements);
    }

    function setAndRemoveError(validationResults, element, condition) {
        if (!condition) {
            validationResults.push(false);
            element.style.borderColor = 'red';
        } else {
            validationResults.push(true);
            element.style.border = 'none';
        }
    }

    function submitData(event) {
        event.preventDefault();
        const validationResults = [];

        setAndRemoveError(
            validationResults,
            inputElements.username,
            regexPatterns.username.test(inputElements.username.value),
        );

        setAndRemoveError(
            validationResults,
            inputElements.email,
            regexPatterns.email.test(inputElements.email.value),
        );

        setAndRemoveError(
            validationResults,
            inputElements.password,
            regexPatterns.password.test(inputElements.password.value),
        );

        setAndRemoveError(
            validationResults,
            inputElements.confirmPassword,
            (inputElements.password.value == inputElements.confirmPassword.value) &&
            inputElements.confirmPassword.value != '',
        );

        if (companyCheckboxElement.checked) {
            setAndRemoveError(
                validationResults,
                inputElements.companyNumber,
                inputElements.companyNumber.value > 1000 &&
                inputElements.companyNumber.value < 9999
            );
        }
        
        if (validationResults.every(x => x == true)) {
            resultDivElement.style.display = 'block';
        } else {
            resultDivElement.style.display = 'none';
        }
    }
}
