function passwordValidation(password) {
    function isLetter(symbol) {
        return (symbol.charCodeAt(0) > 64 && symbol.charCodeAt(0) < 91) ||
                (symbol.charCodeAt(0) > 96 && symbol.charCodeAt(0) < 123);
    }
    
    function isDigit(symbol) {
        return symbol.charCodeAt(0) > 47 && symbol.charCodeAt(0) < 58;
    }

    function checkLength(password) {
        return password.length > 6 && password.length < 10
    }  

    function checkIfContainsOnlyDigitsAndLetters(password) {
        for (let symbol of password) {
            if (!(isDigit(symbol) || isLetter(symbol))) {
                return false
            }
        }

        return true;
    }

    function checkIfPasswordContainsAtLeast2Digits(password) {
        let digitsCounter = 0;

        for (let symbol of password) {
            if (isDigit(symbol)) {
                digitsCounter++;
            }

            if (digitsCounter == 2) {
                return true;
            }
        }

        return false;
    }

    let isValid = true;

    if (!checkLength(password)) {
        console.log('Password must be between 6 and 10 characters');
        isValid = false;
    }

    if (!checkIfContainsOnlyDigitsAndLetters(password)) {
        console.log('Password must consist only of letters and digits');
        isValid = false;
    }

    if (!checkIfPasswordContainsAtLeast2Digits(password)) {
        console.log('Password must have at least 2 digits');
        isValid = false;
    }

    if (isValid) {
        console.log('Password is valid');
    }
}

passwordValidation('logIn');
