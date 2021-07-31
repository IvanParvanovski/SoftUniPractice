function storeProvision(firstArray, secondArray) {
    let store = {};
    
    for (let i = 0; i < firstArray.length; i += 2) {
        let storeProduct = firstArray[i];
        let storeProductQuantity = Number(firstArray[i + 1])
       
        store[storeProduct] = storeProductQuantity;
    }

    for (let i = 0; i < secondArray.length; i += 2) {
        let truckProduct = secondArray[i];
        let truckProductQuantity = Number(secondArray[i + 1]);

        if (Object.keys(store).includes(truckProduct)) {
            store[truckProduct] += truckProductQuantity;
        } else {
            store[truckProduct] = truckProductQuantity;
        }
    }

    for (let product in store) {
        console.log(`${product} -> ${store[product]}`);
    }
}

storeProvision(
    ['Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'],
    ['Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30']);
