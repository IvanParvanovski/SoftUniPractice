function towns(input) {
    for (let townStr of input) {
        let townData = townStr.split(' | ');
        
        let city = {
            town: townData[0],
            latitude: Number(townData[1]).toFixed(2),
            longitude: Number(townData[2]).toFixed(2),
        }

        console.log(city);
    }
}

towns(['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.3363626']);

