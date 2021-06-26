function multiplyNumbers(firstNum, secondNum, thirdNum) {
    function getMultiplicationState(numOne, numTwo) {
        let isPositive = num => num >= 0;
        let areBothNumbersPositive = isPositive(numOne) && isPositive(numTwo);
        let areBothNumbersNegative = !isPositive(numOne) && !isPositive(numTwo);

        return areBothNumbersPositive || areBothNumbersNegative ? 1 : -1 
    }

    let isNegativeOrPositive = getMultiplicationState(
        getMultiplicationState(firstNum, secondNum),
        thirdNum
    );
        
    return isNegativeOrPositive == -1 ? 'Negative' : 'Positive';
}

console.log(multiplyNumbers(5, 12, -15));
console.log(multiplyNumbers(-6, -12, 14));
console.log(multiplyNumbers(-1, -2, -3));
console.log(multiplyNumbers(-5, 1, 1));
