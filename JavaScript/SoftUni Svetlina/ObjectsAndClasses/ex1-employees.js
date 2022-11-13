function employees(namesArray) {
    const result = {};

    for (const name of namesArray) {
        result[name] = name.length;
    }

    for (const kvp of Object.entries(result)) {
        console.log(`Name: ${kvp[0]} -- Personal Number: ${kvp[1]}`);
    }
}

employees([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
]);
