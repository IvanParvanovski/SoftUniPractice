function magicMatrices(input) {
    function isMagic(matrix) {
        let previousRowSum;
        let previousColSum;

        for (let i = 0; i < matrix.length; i++) {
            let rowSum = matrix[i].reduce((total, number) => total += number);
            
            let colSum = 0;
    
            for (let k = 0; k < matrix.length; k++) {
                colSum += matrix[k][i];
            }
    
            if (rowSum != colSum ||
                ((rowSum != previousRowSum || colSum != previousColSum) && 
                i != 0)) {
                
                return false;
            }

            previousRowSum = rowSum;
            previousColSum = colSum;
        }
        return true;
    }
    
    console.log(isMagic(input));
}

console.log(magicMatrices([[4, 5, 6],
    [6, 5, 4],
    [5, 5, 5]]
   ));

// console.log(magicMatrices([
//     [11, 32, 45],
//     [21, 0, 1],
//     [21, 1, 1]
// ]));
