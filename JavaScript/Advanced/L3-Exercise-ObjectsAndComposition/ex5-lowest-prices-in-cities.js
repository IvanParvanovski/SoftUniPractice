function lowestPricesInCities(input) {
    let products = {};

    for (const townData of input) {
        const [town, product, price] = townData.split(' | ');
        if (!(product in products)) {
            products[product] = {};
        }
      
        products[product][town] = Number(price);
    }


    for (const product in products) {
        const sortedTowns = Object.entries(products[product]).sort((a, b) => {
            return a[1] - b[1];
        });

        const cheapestTown = sortedTowns[0];
        console.log(`${product} -> ${cheapestTown[1]} (${cheapestTown[0]})`);
    }   
}

lowestPricesInCities([
    'Sofia City | Audi | 100000',
    'Sofia City | BMW | 100000',
    'Sofia City | Mitsubishi | 10000',
    'Sofia City | Mercedes | 10000',
    'Sofia City | NoOffenseToCarLovers | 0',
    'Mexico City | Audi | 1000',
    'Mexico City | BMW | 99999',
    'New York City | Mitsubishi | 10000',
    'New York City | Mitsubishi | 1000',
    'Mexico City | Audi | 100000',
    'Washington City | Mercedes | 1000',]);
