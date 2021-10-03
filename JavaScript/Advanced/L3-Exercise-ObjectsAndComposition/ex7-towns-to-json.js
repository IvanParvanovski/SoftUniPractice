function townsToJSON(input) {
    let keys = (' ' + input.shift() + ' ').split(' | ');
    keys.shift();
    keys.pop();

    const towns = [];
    const keysLength = keys.length;

    for (const townData of input) {
        let townTokens = (' ' + townData + ' ').split(' | ');
        townTokens.shift();
        townTokens.pop();
        
        let result = {};
        for (let i = 0; i < keysLength; i++) {
            let element = townTokens[i];
            
            if (!isNaN(element)) {
                element = Number(Number(element).toFixed(2));
            }

            result[keys[i]] = element;
        }

        towns.push(result);
    }

    console.log(JSON.stringify(towns));
}

console.log(townsToJSON([
    '| Town | Latitude | Longitude |',
    '| Sofia | 42.696552 | 23.32601 |',
    '| Beijing | 39.913818 | 116.363625 |',
]));
