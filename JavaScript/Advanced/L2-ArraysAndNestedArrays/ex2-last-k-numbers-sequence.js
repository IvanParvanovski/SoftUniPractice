function lastNumbersSequence(n, k) {
    if (n == 0) {
        return [];
    }

    let sequence = [1];

    for (let i = 1; i < n; i++) {
        let diff = i - k;
        
        if (diff < 0) {
            diff = 0;
        }

        let newNum = sequence
                        .slice(diff, i)
                        .reduce((previousValue, currentValue) => previousValue + currentValue);
        
        sequence.push(newNum);
    }

    return sequence;
}

lastNumbersSequence(6, 3);