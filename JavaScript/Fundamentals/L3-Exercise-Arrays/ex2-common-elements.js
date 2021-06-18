function commonElements(firstArray, secondArray) {
    let result = [];

    for (let item of firstArray) {
    
        if (secondArray.includes(item)) {
            result.push(item);
        }
    }

    console.log(result.join('\n'));
}

commonElements(
    ['Hey', 'hello', 2, 4, 'Peter', 'e'],
    ['Petar', 10, 'hey', 4, 'hello', '2']);

commonElements(
    ['S', 'o', 'f', 't', 'u', 'n', 'i'],
    ['s', 'o', 'c', 'i', 'a', 'l'],
)

