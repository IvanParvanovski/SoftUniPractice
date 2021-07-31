function makeDictionary(input) {
    let dictionary = [];

    for (let jsonObject of input) {
        let newObject = JSON.parse(jsonObject);
        let newObjectKey = Object.keys(newObject)[0];

        let exists = dictionary.find(x => Object.keys(x)[0] == newObjectKey);

        if (exists) {
            exists[Object.keys(exists)] = newObject[newObjectKey];
        } else {
            dictionary.push(newObject);
        }
    }

    dictionary.sort((a, b) => {
        let aKey = Object.keys(a)[0].toUpperCase();
        let bKey = Object.keys(b)[0].toUpperCase();

        return aKey.localeCompare(bKey);
    });

    for (let wordObject of dictionary) {
        let word = Object.keys(wordObject)[0];
        console.log(`Term: ${word} => Definition: ${wordObject[word]}`);
    }
}

makeDictionary([
    '{"a": "letter"}',
    '{"a": "hi"}',
    '{"b": "letter"}',
    '{"c": "letter"}',
]);
