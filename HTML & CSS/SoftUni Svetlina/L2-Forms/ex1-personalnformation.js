function displayData() {
    const firstName = document.getElementById('firstName').value;
    const secondName = document.getElementById('secondName').value;
    const lastName = document.getElementById('lastName').value;
    const phoneNumber = document.getElementById('phoneNumber').value;
    const resultElement = document.getElementById('result');
    
    const isNeededInformationGiven = [firstName, secondName, lastName, phoneNumber].every(x => x != '');
    resultElement.style.display = 'block';

    if (isNeededInformationGiven) {
        document.getElementById('resultFullName').textContent = `${firstName} ${secondName} ${lastName}`;
        document.getElementById('resultPhoneNumber').textContent = phoneNumber;
    } else {
        resultElement.innerHTML = '<h1>Invalid Data!</h1>';
    }
}