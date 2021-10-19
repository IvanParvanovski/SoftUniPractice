function subSum(numbers, startIndex, endIndex) {
    if (Array.isArray(numbers) == false) {
        return NaN;
    }

    if (startIndex < 0) {
        startIndex = 0;
    }

    if (endIndex > numbers.length - 1) {
        endIndex = numbers.length - 1;
    }
    
    let total = 0;

    for (let i = startIndex; i < endIndex + 1; i++) {
        total += Number(numbers[i]);
    }

    return total;
} 

subSum([10, 20, 30, 40, 50, 60], -1, 5);
subSum([1.1, 2.2, 3.3, 4.4, 5.5], -3, 1);
subSum([10, 'twenty', 30, 40], 0, 2);
subSum([], 1, 2);
subSum('text', 0, 2);
