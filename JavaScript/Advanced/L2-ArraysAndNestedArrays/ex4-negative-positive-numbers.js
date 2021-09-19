function negativePositiveNumbers(sequence) {
    for (let i = 0; i < sequence.length; i++) {
        let currentElement = sequence[i];

        if (currentElement < 0) {
            for (let pastIndex = i - 1; pastIndex > -1; pastIndex--) {
                if (sequence[pastIndex] < currentElement) {
                    if (currentElement > 0) {
                        break;
                    }
                }
  
                let previousValue = sequence[pastIndex];
                sequence[pastIndex] = currentElement;
                sequence[pastIndex + 1] = previousValue;
            }
        }
    }

    console.log(sequence.join('\n'))
}

negativePositiveNumbers([3, -2, 0, -1]);
negativePositiveNumbers([7, -2, 8, 9]);