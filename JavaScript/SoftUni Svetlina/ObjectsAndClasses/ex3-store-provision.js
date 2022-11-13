function storeProvision(storageArray, deliveryArray) {
    const items = {}

    for (let i = 0; i < storageArray.length; i += 2) {
        items[storageArray[i]] = Number(storageArray[i + 1]);
    }

    for (let i = 0 ; i < deliveryArray.length; i += 2) {
        const key = deliveryArray[i];

        if (!(key in items)) {
            items[key] = 0;
        }

        items[key] += Number(deliveryArray[i + 1]);
    }

    for (const kvp of Object.entries(items)) {
        console.log(`${kvp[0]} -> ${kvp[1]}`);
    }
}

storeProvision(
    [
        'Chips', '5', 
        'CocaCola', '9', 
        'Bananas', '14', 
        'Pasta', '4', 
        'Juice', '2'
    ], 
    [
        'Flour', '44', 
        'Oil', '12', 
        'Pasta', '7', 
        'Tomatoes', '70', 
        'Bananas', '30'
    ]
);
    