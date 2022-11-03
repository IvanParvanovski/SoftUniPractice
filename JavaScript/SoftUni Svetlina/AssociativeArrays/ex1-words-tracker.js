function wordTracker(inputArray) {
    const inputValues = inputArray.shift();
    const searchedValues = inputValues.split(' ').map(x => x.toLocaleLowerCase());
    const res = {};
    
    for (const val of searchedValues) {
        res[val] = 0;
    }

    for (const element of inputArray) {
        const elementLower = element.toLocaleLowerCase() 

        if (searchedValues.includes(elementLower)) {
            res[elementLower] += 1;
        }
    }

    Object.entries(res).sort((a, b) => b[1] - a[1]).forEach(kvp => {
        console.log(`${kvp[0]} - ${kvp[1]}`);
    });
}

wordTracker([
    'Ivan Nikolai Stefan',
    'Ivan', 'Nikolai', 'This', 'is', 'ivan', 'nikolai',
    '',
]);



