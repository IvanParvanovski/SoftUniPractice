function oddAndEvenSum(number) {  
    let numberAsString = number.toString();
    let oddSum = 0;
    let evenSum = 0;

    for (let digitAsString of numberAsString) {
        let digit = Number(digitAsString);

        if (digit % 2 == 0) {
            evenSum += digit;
        } else {
            oddSum += digit;
        }
    }

    return `Odd sum = ${oddSum}, Even sum = ${evenSum}`;
}

console.log(oddAndEvenSum(1000435));
