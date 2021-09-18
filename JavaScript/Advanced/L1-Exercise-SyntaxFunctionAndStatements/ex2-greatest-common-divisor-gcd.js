function greatestCommonDivisor(firstNum, secondNum) {
    while (firstNum != secondNum) {
        if (firstNum > secondNum) { 
            firstNum -= secondNum;
        } else {
            secondNum -= firstNum;
        } 
    }

    console.log(firstNum);
}

greatestCommonDivisor(48, 18);
greatestCommonDivisor(15, 5);
greatestCommonDivisor(2154, 458);
