function equalNeighbors(input) {
    let sides = {
        'left': (row, col) => [row, col - 1],
        'right': (row, col) => [row, col + 1],
        'down': (row, col) => [row + 1, col],
        'up': (row, col) => [row - 1, col], 
    };

    let counter = 0;

    for (let row = 0; row < input.length; row++) {
        for (let col = 0; col < input.length; col++) {
            let currentElement = input[row][col];

            for (let sideTokens of Object.entries(sides)) {
                let [side, sideFunction] = sideTokens;
                let [newRow, newCol] = sideFunction(row, col);

                if ((newRow > -1 && newCol > -1) && 
                    (newRow < input.length && newCol < input[0].length)) {

                    let newElement = input[newRow][newCol];

                    if (newElement == currentElement) {
                        counter++;
                    }
                }
                
            }
        }
    }
    console.log(counter / 2);
}

equalNeighbors([['test', 'yes', 'yo', 'ho'],
['well', 'done', 'yo', '6'],
['not', 'done', 'yet', '5']]
);
