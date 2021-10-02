function townPopulation(input) {
    let towns = {};

    for (const townData of input) {
        const townTokens = townData.split(' <-> ');
        const town = townTokens[0];
        const population = Number(townTokens[1]);
        
        if (!(town in towns)){
            towns[town] = 0;
        }
        
        towns[town] += population;
    }

    for (const [town, population] in Object.entries(towns)) {
        console.log(`${town} : ${population}`);
    }
}

townPopulation(['Sofia <-> 1200000',
'Montana <-> 20000',
'New York <-> 10000000',
'Washington <-> 2345000',
'Las Vegas <-> 1000000']);
