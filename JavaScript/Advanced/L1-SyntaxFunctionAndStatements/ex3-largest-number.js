function largestNumber(firstNum, secondNum, thirdNum) {
    let result = firstNum;

    if (secondNum > result) {
        result = secondNum;
    }

    if (thirdNum > result) {
        result = thirdNum;
    }

    console.log(`The largest number is ${result}.`);
}

function largestNumber(firstNum, secondNum, thirdNum) {
    console.log(`The largest number is ${Math.max(firstNum, secondNum, thirdNum)}.`);
}

largestNumber(5, 10, 2);

