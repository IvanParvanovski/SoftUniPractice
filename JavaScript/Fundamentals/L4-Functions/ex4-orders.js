function calculateTotalPrice(product, quantity) {
    let result = (price) => price * quantity;
    let price;

    switch (product) {
        case 'coffee':
            price = 1.50;
            break;
        case 'water':
            price = 1.00;
            break;
        case 'coke':
            price = 1.40;
            break;
        case 'snacks':
            price = 2.00
            break;
        default:
            price = 0.00;
            break;
    }  

    return result(price).toFixed(2);
}

console.log(calculateTotalPrice('water', 5));
