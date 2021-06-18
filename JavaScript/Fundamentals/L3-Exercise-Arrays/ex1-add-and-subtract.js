function addAndSubtract(numbers) {
    let originalSum = 0;
    let modifiedSum = 0;

    for (let i = 0; i < numbers.length; i++) {
        let num = numbers[i];
    
        if (num % 2 == 0) {
            numbers[i] += i;
        } else {
            numbers[i] -= i;
        }
        originalSum += num;
        modifiedSum += numbers[i];
    }

    console.log(numbers);
    console.log(originalSum);
    console.log(modifiedSum);
}

addAndSubtract([5, 15, 23, 56, 35]);