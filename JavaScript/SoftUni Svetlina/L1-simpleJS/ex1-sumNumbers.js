function sumNumbers(input) {
    console.log(input.reduce((total, currentVal)  => {
        return total + Number(currentVal);
    }, 0));
}

sumNumbers([1, 2, 3, 4, 5, 6, 7]);
sumNumbers([3, 4, 5, 6, 7]);
sumNumbers([1, 2, 3, 4, 5, 6, 7]);
sumNumbers([1, 2, 3, 4, 5, 6, 7]);
