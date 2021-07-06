function negativeOrPositiveNumber(numbers) {
    let result = [];

    for (let num of numbers) {
        if (num < 0) {
            result.unshift(num);
        } else {
            result.push(num);
        }
    }

    return result.join('\n');
}

console.log(negativeOrPositiveNumber([7, -2, 8, 9]));