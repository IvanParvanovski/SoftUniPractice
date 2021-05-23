function printSum(firstNum, secondNum) {
    let total = 0;
    let result = '';
    for (let i = firstNum; i <= secondNum; i++) {
        total += i;
        result += i + ' ';
    }
    console.log(result);
    console.log(`Sum: ${total}`);
}

printSum(5, 10);
printSum(0, 26);
printSum(50, 60);
