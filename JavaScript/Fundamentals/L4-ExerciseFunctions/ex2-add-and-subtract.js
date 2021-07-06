function addAndSubtract(firstNum, secondNum, thirdNum) {
    function sum(firstUnit, secondUnit) {
        return firstUnit + secondUnit;
    }   

    function subtract(firstUnit, secondUnit) {
        return firstUnit - secondUnit;
    }

    return subtract(sum(firstNum, secondNum), thirdNum);

}

console.log(addAndSubtract(2, 3, 1));
