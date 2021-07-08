function uniqueElements(elements) {
    let result = [];

    for (let element of elements) {
        if (!result.includes(element)) {
            result.push(element);
        }
    }

    console.log(result.join(' '));
}

uniqueElements([1, 2, 3, 4, 5, 6,
                1, 2, 3, 4, 5, 6,]);