function displayData() {
    const firstNameElement = document.getElementById('firstName');
    const firstName = firstNameElement.value;

    const secondNameElement = document.getElementById('secondName');
    const secondName = secondNameElement.value;

    const lastNameElement = document.getElementById('lastName');
    const lastName = lastNameElement.value;
    
    const phoneNumberElement = document.getElementById('phoneNumber');
    const phoneNumber = phoneNumberElement.value;

    const resultElement = document.getElementById('result');
    
    const isNeededInformationGiven = [firstName, secondName, lastName, phoneNumber].every(x => x != '');
    resultElement.style.display = 'block';

    if (isNeededInformationGiven) {
        document.getElementById('resultFullName').textContent = `${firstName} ${secondName} ${lastName}`;
        document.getElementById('resultPhoneNumber').textContent = phoneNumber;
    } else {
        resultElement.innerHTML = '<h1>Invalid Data!</h1>';
    }

    firstNameElement.value = '';
    secondNameElement.value = '';
    lastNameElement.value = '';
    phoneNumberElement.value = '';

}