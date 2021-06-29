function printMatrix(num) {
    let result = '';

    for (let row = 0; row < num; row++) {
        for (let col = 0; col < num; col++) {
            result += num + ' ';
        }
        result += '\n'
    }

    console.log(result);
}

printMatrix(3);