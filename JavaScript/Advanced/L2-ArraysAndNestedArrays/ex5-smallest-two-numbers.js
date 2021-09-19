function getTheTwoSmallestNumbers(sequence) {
    let sortedSequence = sequence.sort((a, b) => a - b); // O(n * log(n))
    console.log(sortedSequence[0], sortedSequence[1]); // O(1)
}


function getTheTwoSmallestNumbers2(sequence) {
    function getTheSmallestNumber(seq) {
        return Math.min(...seq); // O(n)
    }

    // O(1)
    let neededAmount = 2;

    // O(n)
    for (let i = 0; i < neededAmount; i++) {
        let smallestNumber = getTheSmallestNumber(sequence); // O(n)
        let index = sequence.indexOf(smallestNumber); // O(n)
        sequence.splice(index, 1); // O(n)

        console.log(smallestNumber); // O(1)
    }

    console.log();
}

getTheTwoSmallestNumbers2([30, 15, 50, 5]);
