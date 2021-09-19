function processOddPositions(numbers) {
    let oddNumbers = [];

    for (let i = 1; i < numbers.length; i += 2) {
        oddNumbers.push(numbers[i]);
    }

    let doubledOddNumbers = oddNumbers.map(x => x * 2);
    let reverseOddNumbers = doubledOddNumbers.reverse();

    console.log(reverseOddNumbers.join(' '));
}

processOddPositions([10, 15, 20, 25]);
