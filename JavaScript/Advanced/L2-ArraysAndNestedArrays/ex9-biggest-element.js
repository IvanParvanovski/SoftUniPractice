function biggestElement(input) {
    let biggestItem = Number.NEGATIVE_INFINITY; 

    for (let sequence of input) {
        let currentBiggestElement = Math.max(...sequence);
        
        if (currentBiggestElement > biggestItem) {
            biggestItem = currentBiggestElement;
        }
    }
    
    console.log(biggestItem);
    
}

biggestElement([
    [-1, -4, -10],
    [-18, -20, -15],
]);
