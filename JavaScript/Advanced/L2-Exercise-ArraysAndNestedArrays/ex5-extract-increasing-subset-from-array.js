function extractIncreasingSequence(numbers) {
    let lastBiggestNum = Number.MIN_SAFE_INTEGER;
    
    let result = numbers.filter((x) => {
        if (x >= lastBiggestNum) {
            lastBiggestNum = x;
            return true;
        }
        return false;
    });

    return result;
}

console.log(extractIncreasingSequence([1, 3, 8, 4, 10, 12, 3, 2, 24]));
console.log(extractIncreasingSequence([ ]));
