function calculator(firstNum, operator, secondNum) {
    const operations = {
        '+': (a, b) => a + b,
        '-': (a, b) => a - b,
        '*': (a, b) => a * b,
        '/': (a, b) => a / b,
    };

    if (secondNum == '0' && operator == '/') {
        console.log('Can\'t divide by 0!');
        return;
    }

    console.log(operations[operator](Number(firstNum), Number(secondNum)));
}

calculator(2, '+', 2);
calculator(0, '/', 1);
calculator(2, '*', 2);
calculator(4, '/', 2);