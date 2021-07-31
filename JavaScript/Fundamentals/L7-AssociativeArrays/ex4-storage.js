function storage(items) {
    let warehouse = new Map();

    for (let itemData of items) {
        let itemInfo = itemData.split(' ');
        
        let productName = itemInfo[0];
        let productQuantity = Number(itemInfo[1]);

        if (!warehouse.has(productName)) {
            warehouse.set(productName, 0);
        }

        warehouse.set(productName, warehouse.get(productName) + productQuantity);
    }

    for (let [item, quantity] of warehouse) {
        console.log(`${item} -> ${quantity}`);
    }
}

storage([
    'tomatoes 10',
    'coffee 5',
    'olives 100',
    'coffee 40',
])