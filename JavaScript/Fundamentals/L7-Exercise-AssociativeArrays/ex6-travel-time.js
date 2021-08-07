function travel(input) {
    // Keep the offers 
    let offers = {};    

    // Iterate threw the given offers and store them
    for (let offer of input) {
        let [country, city, price] = offer.split(' > ');
        price = Number(price);

        // Check if the country exists, if not add it
        if (!(country in offers)) {
            offers[country] = {};
        }

        // Check if the town exists, if it does set the lower offer
        if (city in offers[country]) {
            let currentPrice = offers[country][city];

            if (currentPrice > price) {
                offers[country][city] = price;
            }
        } else {
            offers[country][city] = price;
        }
    }

    // Sort the offers alphabetically and then by lowest travel cost
    let sortedOffersAphabetically = Object.entries(offers).sort((a, b) => a[0].localeCompare(b[0]));

    for (let [country, destinations] of sortedOffersAphabetically) {
        let output = country + ' -> ';

        // Sort the destinations by the lowest price
        let sortedDestinations = Object.entries(destinations).sort((a, b) => a[1] - b[1]);
        
        sortedDestinations.forEach(destinationData => {
            let destinationsOutput = destinationData.join(' -> ');
            output += destinationsOutput + ' '; 
        })
        
        console.log(output);
    }
}

travel([
    'Bulgaria > Sofia > 500',
    'Bulgaria > Sopot > 800',
    'France > Paris > 2000',
    'Albania > Tirana > 1000',
    'Bulgaria > Sofia > 200',
]);
