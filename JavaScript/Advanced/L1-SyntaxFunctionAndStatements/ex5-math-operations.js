function mathOperations(num1, num2, operator) {
    let operators = {
        '+': (num1, num2) => num1 + num2,
        '-': (num1, num2) => num1 - num2,
        '*': (num1, num2) => num1 * num2,
        '/': (num1, num2) => num1 / num2,
        '%': (num1, num2) => num1 % num2,
        '**': (num1, num2) => num1 ** num2,
    }

    console.log(operators[operator](num1, num2));
}

mathOperations(5, 6, '+');
