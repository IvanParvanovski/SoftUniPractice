function displayTriangle(num) {
    let result = '';

    for (let row = 1; row <= num; row++) {
        for (let col = 0; col < row; col++) {
            result += row + ' ';
        }
        result += '\n';
    }
    console.log(result);
}
displayTriangle(3);
