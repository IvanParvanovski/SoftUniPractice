function sortingArrays(array) {
    let sortedArray = array.sort((a, b) => a - b);    
    let result = [];
    let n = Math.ceil(sortedArray.length / 2);

    for (let i = 0; i < n; i++) {
        result.push(array[sortedArray.length - i - 1]);    

        if (sortedArray.length % 2 != 0 && i == n - 1) {
            break;
        }

        result.push(array[i]);
    }

    console.log(result.join(' '));
}

sortingArrays([1, 2, 3]);
sortingArrays([1, 21, 3, 52, 69, 63, 31, 2, 18, 94]);