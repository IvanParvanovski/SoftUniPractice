function calculator(numOne, numTwo, operator) {
    let operators = {
        'multiply': '*',
        'divide': '/',
        'add': '+',
        'subtract': '-',
    };

    let result = o => eval(`${numOne} ${o} ${numTwo}`) 
    return result(operators[operator]);
}

console.log(calculator(5, 5, 'multiply'));
