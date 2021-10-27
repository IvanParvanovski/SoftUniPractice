function maxAndMin(numbers) {
    const sortedNumbers = numbers.sort((a, b) => a - b);
    console.log(sortedNumbers[0]);
    console.log(sortedNumbers.slice(-1)[0]);
}

maxAndMin([42, 21, 16, 476, 1236]);
