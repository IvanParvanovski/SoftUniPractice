function mining(input) {
    let sources = {};

    // Iterate threw each input array where
    // Every ODD is the source 
    // Every EVEN is the quantity

    // Check if the source already exists and if it does increase it
    // Otherwise just add it and set it's quantity

    for (let index = 0; index < input.length; index += 2) {
        let source = input[index];
        let quantity = input[index + 1];

        if (!(source in sources)) {
            sources[source] = 0;
        }

        sources[source] += Number(quantity);
    }

    for (let [source, quantity] of Object.entries(sources)) {
        console.log(`${source} -> ${quantity}`);
    }
}

mining([
    'Gold',
    '155',
    'Silver',
    '10',
    'Copper',
    '17',
]);

mining([
    'gold',
    '155',
    'silver',
    '10',
    'copper',
    '17',
    'gold',
    '15'
        
])