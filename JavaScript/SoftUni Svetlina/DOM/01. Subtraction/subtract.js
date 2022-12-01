function subtract() {
    const firstInput = document.getElementById('firstNumber');
    const secondInput = document.getElementById('secondNumber');
    const result = document.getElementById('result');

    result.textContent = Number(firstInput.value) - Number(secondInput.value);
}

subtract();