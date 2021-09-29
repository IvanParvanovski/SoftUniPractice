function sortingNumbers(numbers) {
    let sortedNumbers = numbers.sort((a, b) => a - b);
    let result = [];

    // while (sortedNumbers.length > 0) {
    //     let smallestNum = sortedNumbers.shift();
    //     result.push(smallestNum);
        
    //     if (sortedNumbers.length >= 1) {
    //         let biggestNum = sortedNumbers.pop();
    //         result.push(biggestNum);
    //     }
    // }

    while (sortedNumbers.length != 0) {
        result.push(sortedNumbers.shift(), sortedNumbers.pop());
    }

    return result;
}

console.log(sortingNumbers([1, 2, 3]));
