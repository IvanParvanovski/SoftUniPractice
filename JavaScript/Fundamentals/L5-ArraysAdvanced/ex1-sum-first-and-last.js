function firstAndLastNumbersSum(numbers) {
    let firstNum = Number(numbers.shift());
    let lastNum = Number(numbers.pop());
    
    return firstNum + lastNum;
}

console.log(firstAndLastNumbersSum(['5', '10', '15']));
