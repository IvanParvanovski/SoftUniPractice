function mergeArrays(firstArray, secondArray) {
    let result = [];

    for (let i = 0; i < firstArray.length; i++) {
        let firstElement = firstArray[i];
        let secondElement = secondArray[i];

        if (i % 2 == 0) {
            result.push(Number(firstElement) + Number(secondElement));
        } else {
            result.push(firstElement + secondElement);
        }
    }

    console.log(result.join(' - '));
}

mergeArrays(['5', '15', '23', '56', '35'],
            ['17', '22', '87', '36', '11']);