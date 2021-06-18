function ladyBugs(input) {
    let fieldSize = input.shift();
    let bugsPositions = input.shift().split(' ');

    let field = [];
    for (let i = 0; i < fieldSize; i++) {
        if (i == bugsPositions[0]) {
            field.push(1);
            bugsPositions.shift();
        } else {
            field.push(0);
        }
    }
    
    for (let move of input) {
        let moveData = move.split(' ');
        
        // Read data
        let bugIndex = Number(moveData[0]);
        let direction = moveData[1];
        let steps = Number(moveData[2]);
        
        // Check if bug index is valid and
        // Check if on the bug index there is a bug
        if (bugIndex >= 0 && bugIndex < fieldSize && field[bugIndex] == 1) {
            let baseIndex = bugIndex;

            // Change the position of the bug
            while (true) {
                // Check if the bug has landed on 0
                if (field[bugIndex] == 0) {
                    field[bugIndex] = 1;
                    break;
                }

                // Check if the bug has gone outside the field
                if (bugIndex > fieldSize || bugIndex < 0) {
                    field[baseIndex] = 0;
                    break;
                }

                // Change position
                if (direction == 'right') {
                    bugIndex += steps;
                } else if (direction == 'left') {
                    bugIndex -= steps;
                } else {
                    break;
                }
            }

            // Check if the bug is in the field and if it is
            // Set it on the current position
            if (bugIndex >= 0 && bugIndex < fieldSize) {
                field[bugIndex] = 1;
            }

            // Reset the previous position of the bug
            if (baseIndex != bugIndex) {
                field[baseIndex] = 0;   
            }
        }
    }
    console.log(field.join(' '));
}

// ladyBugs([3, '0 1', '0 right 1', '2 right 1']);
// ladyBugs([ 3, '0 1 2','0 right 1', '1 right 1', '2 right 1'] );
// ladyBugs([ 5, '3', '3 left 2', '1 left -2']);

// ladyBugs([3, '0', '0 right 2',
//                   '2 left 2',
//                   '0 left -2',
//                   '0 left 2',
//                   '-5 right 2',
//                   '2 left 100',
//                   '2 right 2']);


console.log(ladyBugs([3, '2', '0 right 1', '1 left 2', '0 right -1', '1 right -2', '0 left 1', '0 left -1', '1 right 1', '1 left -1', '50 right 100', '2 west 5']));
// console.log('---');

console.log(ladyBugs([3, '1', '0 right 1', '1 left 2', '0 right -1', '1 right -2', '0 left 1', '0 left -1', '1 right 1', '1 left -1', '50 right 100', '2 west 5']));
// console.log('---');

console.log(ladyBugs([3, '0', '0 right 1', '1 left 2', '0 right -1', '1 right -2', '0 left 1', '0 left -1', '1 right 1', '1 left -1', '50 right 100', '2 west 5']));
// console.log('---');

console.log(ladyBugs([3, '0 1 2', '0 right 1', '1 left 2', '0 right -1', '1 right -2', '0 left 1', '0 left -1', '1 right 1', '1 left -1', '50 right 100', '2 west 5']));
// console.log('---');

console.log(ladyBugs([3, '', '0 right 1', '1 left 2', '0 right -1', '1 right -2', '0 left 1', '0 left -1', '1 right 1', '1 left -1', '50 right 100', '2 west 5']));
// console.log('---');

console.log(ladyBugs([3, '4', '0 right 1', '1 left 2', '0 right -1', '1 right -2', '0 left 1', '0 left -1', '1 right 1', '1 left -1', '50 right 100', '2 west 5']));
