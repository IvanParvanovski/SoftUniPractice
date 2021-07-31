function neighborhoods(input) {
    let neighborhoods = new Map();

    for (let neighborhood of input.shift().split(', ')) {
        let peopleArr = [];
        neighborhoods.set(neighborhood, peopleArr);
    }

    for (let personInfo of input) {
        let personData = personInfo.split(' - ');
        let searchedNeighborhood = personData[0]; 
        
        if (neighborhoods.has(searchedNeighborhood)) {
            let personNeighborhood = neighborhoods.get(searchedNeighborhood);
            let personName = personData[1];
    
            personNeighborhood.push(personName);
        }
    }

    let sortedNeighborhoods = [...neighborhoods.entries()].sort((a, b) => b[1].length - a[1].length);

    for (let [neighborhood, people] of sortedNeighborhoods) {
        console.log(`${neighborhood}: ${people.length}`);
        for (let person of people) {
            console.log(`--${person}`);
        }
    }
}

neighborhoods([
    'Abbey Street, Herald Street, Bright Mews',
    'Bright Mews - Garry',
    'Bright Mews - Andrea',
    'Invalid Street - Tommy',
    'Abbey Street - Billy',
]);
