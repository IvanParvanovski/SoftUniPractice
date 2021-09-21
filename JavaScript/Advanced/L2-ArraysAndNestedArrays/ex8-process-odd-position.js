function processOddPositions(numbers) {
    let oddNumbers = numbers.filter((v, i) => i % 2 != 0);
    let doubledOddNumbers = oddNumbers.map(x => x * 2);
    let reverseOddNumbers = doubledOddNumbers.reverse();

    console.log(reverseOddNumbers.join(' '));

    // console.log(numbers
    //     .filter((v, i) => i % 2 != 0)
    //     .map((x) => x * 2)
    //     .reverse()
    //     .join(' ')
    // );
}

processOddPositions([10, 15, 20, 25]);
