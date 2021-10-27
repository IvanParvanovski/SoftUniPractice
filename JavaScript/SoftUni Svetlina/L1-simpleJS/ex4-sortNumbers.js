let numbers = [
    [2, -1, 15],
    [3, 15, 18],
];

function sortArray() {
    for (const arr of numbers) {
        arr.sort((a, b) => a - b);
        console.log(arr.join(' '));
    }
}

sortArray();
