function argumentInfo(...args) {
    const types = {};

    function addElement(type) {
        if (!(type in this)) {
            this[type] = 0;
        }

        this[type] += 1; 
    }
   
    const addType = addElement.bind(types);

    for (const value of args) {
        const type = typeof(value);
        addType(type);
        console.log(`${type}: ${value}`);
    }

    const sortedTypes = Object.entries(types)
        .sort((a, b) => {
            const aAsString = a.toString();
            const bAsString = b.toString();

            if (a[1] != b[1]) {
                return bAsString.localeCompare(aAsString);
            }
        });

    
    for (const typeTokens of sortedTypes) {
        const [type, count] = typeTokens;
        console.log(`${type} = ${count}`);
    }
}

argumentInfo(1, 1, '1', [], []);


// var expectedOutput = [
//     'object:',
//     'number: 3.333',
//     'number: 9.999',
//     'number = 2',
//     'object = 1'
// ];

// for (var i = 0; i < output.length; i++) {
//     var current = output[i];
//     expect(current).to.contains(expectedOutput[i], "Incorrect number of arguments parsed.");
// }