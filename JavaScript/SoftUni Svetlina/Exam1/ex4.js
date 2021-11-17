function calculator(firstNum, operator, secondNum) {
    const operations = {
        '+': (a, b) => a + b,
        '-': (a, b) => a - b,
        '*': (a, b) => a * b,
        '/': (a, b) => a / b,
    };

    if (secondNum == '0' && operator == '/') {
        return 'Can\'t divide by 0!';
    }

    return operations[operator](Number(firstNum), Number(secondNum));
}

console.log(calculator(2, '+', 2));

console.log(calculator(0, '/', 1));

console.log(calculator(2, '*', 2));

console.log(calculator(4, '/', 2));