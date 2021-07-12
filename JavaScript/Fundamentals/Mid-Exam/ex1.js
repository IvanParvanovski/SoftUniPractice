function solve(input) {
    let quantityFoodInKilos = Number(input.shift()) * 1000;
    let quantityHayInKilos = Number(input.shift()) * 1000;
    let quantityCoverInKilos = Number(input.shift()) * 1000;
    let petWeight = Number(input.shift()) * 1000;

    for (let i = 1; i <= 30; i++) {
        if (quantityCoverInKilos < 0 || quantityHayInKilos < 0 || quantityFoodInKilos < 0) {
            break;
        }

        quantityFoodInKilos -= 300;
        
        if (i % 2 == 0) {
            quantityHayInKilos -= 0.05 * quantityFoodInKilos;
        }

        if (i % 3 == 0) {
            quantityCoverInKilos -= petWeight * 1 / 3;
        }
    }
    
    if (quantityCoverInKilos > 0 && quantityHayInKilos > 0 && quantityFoodInKilos > 0) {
        console.log(`Everything is fine! Puppy is happy! ` +
         `Food: ${(quantityFoodInKilos / 1000).toFixed(2)}, ` +
         `Hay: ${(quantityHayInKilos / 1000).toFixed(2)}, ` +
         `Cover: ${(quantityCoverInKilos / 1000).toFixed(2)}.`);
    } else {
        console.log('Merry must go to the pet store!');
    }
}

solve([1,
    1.5,
    3,
    1.5]);