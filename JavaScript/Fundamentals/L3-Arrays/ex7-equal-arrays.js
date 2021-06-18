function equalArrays(firstArray, secondArray) {
    let total = 0;
    let difference = -1;

    for (let index in firstArray) {
        let firstArrayElement = firstArray[index];
        let secondArrayElement = secondArray[index];

        if (firstArrayElement !== secondArrayElement) {
            difference = index;
            break;
        } else {
            total += Number(firstArrayElement);
        }
    }

    console.log(`Arrays are ${difference == -1
        ? `identical. Sum: ${total}`
        : `not identical. Found difference at ${difference} index`}`);

}

equalArrays(['10', '20', '30'], ['10', '20', '30']);
equalArrays(['1', '2', '3', '4', '5'], ['1', '2', '4', '4', '5']);
equalArrays(['1'], ['10']);
equalArrays([], []);