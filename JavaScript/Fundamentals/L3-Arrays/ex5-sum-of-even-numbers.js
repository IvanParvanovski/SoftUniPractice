function sumNumbers(numbers) {
    let total = 0;
    for (let digit of numbers) {
        if (digit % 2 == 0) {
            total += Number(digit);
        }
    }
    console.log(total);
}

sumNumbers(['1', '2', '3', '4', '5', '6']);
