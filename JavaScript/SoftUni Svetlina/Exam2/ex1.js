function main(inputArray) {
    const evenPositions = [];
    let result = [];
    
    for (let i = 0; i < inputArray.length; i++) {
        result[i] = 'empty';
    }

    for (let i = 0; i < inputArray.length; i++) {
        const number = inputArray[i];

        if (i % 2 != 0) {
            result[i] = number;
        } else {
            evenPositions.push(number);
        }
    }
    
    const sortedEven = evenPositions.sort((a, b) => a - b);

    while (true) {
        if (sortedEven.length == 0) {
            break;
        }

        let currentVal = sortedEven.shift();
        let indexOfEmpty = result.indexOf('empty');

        result[indexOfEmpty] = currentVal;
    }

    return result.join(' ');
}


console.log(main([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]));
// [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]