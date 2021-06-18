function reverseArray(amountOfElments, numbers) {
    
    let resultArray = [];
    for (let i = amountOfElments - 1; i >= 0; i--) {
        resultArray.push(numbers[i]);
    }

    console.log(resultArray.join(' '));
}

reverseArray(4, [1, 2, 3, 4, 5, 6]);
