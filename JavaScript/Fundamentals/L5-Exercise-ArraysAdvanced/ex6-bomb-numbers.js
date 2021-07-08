function bombNumbers(array, bombInfo) {
    let bombNum = bombInfo[0];
    let bombRange = bombInfo[1];

    while (array.includes(bombNum)) {
        let bombIndex = array.indexOf(bombNum);
        let startIndex = bombIndex - bombRange;
        let countOfElementsToDelete = bombRange * 2 + 1;
        array.splice(
            startIndex >= 0 ? startIndex : 0,
            countOfElementsToDelete < array.length ? countOfElementsToDelete : array.length
        );    
    }
    let total = 0;

    for (let num of array) {
        total += num;
    }
    console.log(total);
}
bombNumbers([1, 2, 1], [2, 2]);
// bombNumbers([1, 2, 2, 4, 2, 2, 2, 9], [4, 2]);
// bombNumbers([1, 4, 4, 2, 8, 9, 1], [9, 3]);
// bombNumbers([1, 7, 7, 1, 2, 3], [7, 1]);
// bombNumbers([1, 1, 2, 1, 1, 1, 2, 1, 1, 1], [2, 1]);
