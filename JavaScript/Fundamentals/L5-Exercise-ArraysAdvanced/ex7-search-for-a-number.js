function searchForNumber(numbers, commandsArray) {
    let elementsToTake = commandsArray[0];
    let elementsToDelete = commandsArray[1];
    let elemenetToSearch = commandsArray[2];
    let searchedElementCount = 0;

    for (let i = elementsToDelete; i < elementsToTake; i++) {
        let currentNumber = numbers[i];
        if (currentNumber == elemenetToSearch) {
            searchedElementCount++;
        }
    }

    console.log(`Number ${elemenetToSearch} occurs ${searchedElementCount} times.`);
}

searchForNumber([5, 2, 3, 4, 1, 6], [5, 2, 3]);
searchForNumber([2, 2, 2, 2, 2, 2], [5, 2, 2]);