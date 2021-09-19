function diagonalSum(input) {
    let diagonals = {
        left: {
            startIndex: 0,
            total: 0,
            operation: 1
        },

        right: {
            startIndex: input[0].length - 1,
            total: 0,
            operation: -1
        }
    }

    for (let row = 0; row < input.length; row++) {
        for (let diagonalTokens of Object.entries(diagonals)) {
            let diagonalData = diagonalTokens[1];
            
            diagonalData.total += input[row][diagonalData.startIndex];
            diagonalData.startIndex += diagonalData.operation;
        }
    } 

    let diagonalsSum = Object.entries(diagonals).map(element => {
        return element[1].total;
    }); 
    
    console.log(diagonalsSum.join(' '));
}

diagonalSum([
    [20, 40],
    [10, 60],
]);
