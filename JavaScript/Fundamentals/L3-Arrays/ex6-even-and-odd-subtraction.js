function evenAndOddSubstraction(numbers) {
    let oddSum = 0;
    let evenSum = 0;

    for (let num of numbers) {
        if (num % 2 == 0) {
            evenSum += num;
        } else {
            oddSum += num;
        }    
    }

    console.log(evenSum - oddSum);
}

evenAndOddSubstraction([1, 2, 3, 4, 5, 6]);
