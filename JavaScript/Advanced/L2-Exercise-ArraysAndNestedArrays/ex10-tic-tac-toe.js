function ticTacToe(moves) {
    function checkIsMatch(line, mark) {
        return line.every((x) => x == mark);
    }

    function getColumn(dashBoard, i) {
        let column = [];

        for (let k = 0; k < dashBoard.length; k++) {
            column.push(dashBoard[k][i]);
        }

        return column;
    }

    function getDiagonals(dashBoard) {
        let rightDiagonal = [];
        let leftDiagonal = [];
        const dbl = dashBoard.length;

        for (let i = 0; i < dashBoard.length; i++) {
            leftDiagonal.push(dashBoard[i][i]);
            rightDiagonal.push(dashBoard[i][dbl - i - 1])
        }

        return [leftDiagonal, rightDiagonal];
    }   

    function hasWinner(dashBoard, players) {
        for (let i = 0; i < dashBoard.length; i++) {
            const column = getColumn(dashBoard, i);
            const row = dashBoard[i];
            
            // Check rows
            if (checkIsMatch(row, players.firstPlayer.mark)) {
                return players.firstPlayer;
            } else if (checkIsMatch(row, players.secondPlayer.mark)) {
                return players.secondPlayer;
            }
        
            // Check columns
            if (checkIsMatch(column, players.firstPlayer.mark)) {
                return players.firstPlayer;
            } else if (checkIsMatch(column, players.secondPlayer.mark)) {
                return players.secondPlayer;
            }
        }

        const [leftDiagonal, rightDiagonal] = getDiagonals(dashBoard);

        if (checkIsMatch(leftDiagonal, players.firstPlayer.mark)) {
            return players.firstPlayer;
        } else if (checkIsMatch(leftDiagonal, players.secondPlayer.mark)){
            return players.secondPlayer;
        }

        if (checkIsMatch(rightDiagonal, players.firstPlayer.mark)) {
            return players.firstPlayer;
        } else if (checkIsMatch(rightDiagonal, players.secondPlayer.mark)){
            return players.secondPlayer;
        }

        return undefined;
    }

    function hasFreeSpaces(dashBoard) {
        for (let row of dashBoard) {
            let spaces = row.some((x) => x == false);

            if (spaces) {
                return true;
            }
        }

        return false;
    }

    const dashBoard = [
        [false, false, false],
        [false, false, false],
        [false, false, false],
    ];

    const players = {
        firstPlayer: {
            mark: 'X',
        },

        secondPlayer: {
            mark: 'O',
        }
    };

    let turn = false;
    let winner;
    for (let i = 0; i < moves.length; i++) {
        let move = moves[i];
        let [x, y] = move.split(' ');
   
        let currentMark; 
        if (turn) {
            currentMark = 'O';
        } else {
            currentMark = 'X';
        }

        let status = dashBoard[x][y];
        while (status) {
            console.log('This place is already taken. Please choose another!');
            
            i++;
            move = moves[i];

            [x, y] = move.split(' ');
            status = dashBoard[x][y];
        } 

        dashBoard[x][y] = currentMark;
        
        winner = hasWinner(dashBoard, players);
        
        if (winner != undefined) {
            break;
        }

        let containsFreeSpaces = hasFreeSpaces(dashBoard);

        if (!containsFreeSpaces) {
            break;
        }

        turn = !turn;
    }

    let winnerMessage;
    if (winner != undefined) {
        winnerMessage = `Player ${winner.mark} wins!`;
    } else {
        winnerMessage = 'The game ended! Nobody wins :(';
    }

    console.log(winnerMessage);
    
    for (let row of dashBoard) {
        console.log(row.join('\t'));
    }
}

ticTacToe(["0 1",
"0 0",
"0 2",
"2 0",
"1 0",
"1 2",
"1 1",
"2 1",
"2 2",
"0 0"]);
