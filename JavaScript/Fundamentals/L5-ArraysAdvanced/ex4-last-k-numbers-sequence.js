function lastKNumbersSequence(sequenceLength, amountOfPastElements) {
    function sum(numbers) {
        let total = 0;
        for (let num of numbers) {
            total += num;
        }
        return total;
    }

    let result = [1]
    for (let i = 1; i < sequenceLength; i++) { 
        result.push(sum(result.slice(-amountOfPastElements)));
    }

    console.log(result.join(' '));
}

lastKNumbersSequence(6, 3);