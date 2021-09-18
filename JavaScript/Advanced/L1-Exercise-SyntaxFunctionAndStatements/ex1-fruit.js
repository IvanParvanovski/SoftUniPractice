function buyFruit(fruit, weightInGrams, pricePerKilo) {
    let weightInKilos = weightInGrams / 1000;
    let price = pricePerKilo * weightInKilos;

    console.log(`I need $${price.toFixed(2)} to buy ${weightInKilos.toFixed(2)} kilograms ${fruit}.`);
}

buyFruit('orange', 2500, 1.80);
