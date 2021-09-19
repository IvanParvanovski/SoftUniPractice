function biggerHalf(sequence) {
    return sequence.sort((a, b) => a - b).slice(sequence.length / 2);
}

biggerHalf([4, 7, 2, 5]);
