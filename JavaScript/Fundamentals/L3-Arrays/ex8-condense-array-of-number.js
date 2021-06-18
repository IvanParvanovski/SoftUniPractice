function condenseArray(numbers) {
    
    while (numbers.length > 1)
    {
        let result = [];

        for (let i = 0; i < numbers.length - 1; i++) {
            let currentElement = numbers[i];
            let nextElement = numbers[i + 1];
            result.push(currentElement + nextElement);
        }
    
        numbers = result;
    }
    console.log(numbers[0]);
}

condenseArray([2, 10, 3,]);
condenseArray([5, 0, 4, 1, 2]);
condenseArray([1]);
