function storeCatalogue(input) {
    const products = {};

    for (const productData of input) {
        const [product, price] = productData.split(' : ');
        products[product] = price;
    }

    const sortedProducts = Object.entries(products).sort((a, b) => a[0].localeCompare(b[0]));

    let firstLetter;
    for (const productTokens of sortedProducts) {
        if (firstLetter != productTokens[0][0]) {
            firstLetter = productTokens[0][0];
            console.log(firstLetter);
        }

        console.log('  ' + productTokens.join(': '));
    }
}

storeCatalogue(['Appricot : 20.4',
'Fridge : 1500',
'TV : 1499',
'Deodorant : 10',
'Boiler : 300',
'Apple : 1.25',
'Anti-Bug Spray : 15',
'T-Shirt : 10']);
