function firstAndLastKNumbers(input) {
    let elementsAmount = input.shift();
    
    let firstNumbers = input.slice(0, elementsAmount);  
    let lastNumbers = input.slice(-elementsAmount);  
    
    console.log(firstNumbers.join(' '));
    console.log(lastNumbers.join(' '));
}

firstAndLastKNumbers([2, 7, 8, 9]);
