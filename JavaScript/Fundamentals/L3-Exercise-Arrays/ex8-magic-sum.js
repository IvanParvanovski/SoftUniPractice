function magicSum(numbers, num) {
    let result = [];

    for (let i = 0; i < numbers.length; i++) {
        let mainNum = numbers[i];

        for (let j = i + 1; j < numbers.length; j++) {
            let secondaryNum = numbers[j];

            if (mainNum + secondaryNum == num) {
                result.push([mainNum, secondaryNum]);
            }
        }
    }

    for (let r of result) {
        console.log(r.join(' '));
    }
}

magicSum([1, 7, 6, 2, 19, 23], 8);
console.log('---');
magicSum([14, 20, 60, 13, 7, 19, 8], 27);
console.log('---');
magicSum([1, 2, 3, 4, 5, 6], 6);
