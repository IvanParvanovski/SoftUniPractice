function longestSequence(numbers) {
    let result = [];
    let currentSequence = [];

    for (let num of numbers) {
        if (num != currentSequence[0] && currentSequence.length > 0) {
            if (currentSequence.length > result.length) {
                result = currentSequence;
            }
            currentSequence = [];
        }

        currentSequence.push(num);
    }

    if (currentSequence.length > result.length) {
        result = currentSequence;
    }

    console.log(result.join(' '));
}

longestSequence([2, 1, 1, 2, 3, 3, 2, 2, 2, 1]);
longestSequence([1, 1, 1, 2, 3, 1, 3, 3,]);
longestSequence([4, 4, 4, 4]);
longestSequence([0, 1, 1, 5, 2, 2, 6, 3, 3]);
