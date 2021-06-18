function reverseArrayOfStrings(input) {
    for (let j = 0; j < input.length; j++){
        for (let i = input.length - 1; i > j; i--) {
            let currentValue = input[i];
            input[i] = input[i - 1];
            input[i - 1] = currentValue;
        }
    }
    
    console.log(input.join(' '));
}

reverseArrayOfStrings(['a', 'b', 'c', 'd', 'e']);
