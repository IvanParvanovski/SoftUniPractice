function topIntegers(numbers) {
    let result = [];
    for (let i = 0; i < numbers.length; i++) {
        let shouldAdd = true;
        let currentNum = numbers[i];

        for (let j = i + 1; j < numbers.length; j++) {
            if (currentNum < numbers[j]) {
                shouldAdd = false;
                break;
            }
        }

        if (shouldAdd) {
            if (!result.includes(currentNum)) {
                result.push(currentNum);
            }
        }
    }
    console.log(result.join(' '));
}

topIntegers([1, 4, 3, 2]);
topIntegers([14, 24, 3, 19, 15, 17]);
topIntegers([41, 41, 34, 20]);