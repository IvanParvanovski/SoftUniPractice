function calorieObject(foods) {
    let products = {};

    for (let i = 0; i < foods.length; i += 2) {
        let product = foods[i];
        let calories = foods[i + 1];

        products[product] = Number(calories);
    }

    console.log(products);
}

calorieObject(['Yoghurt', '48', 'Rise', '138', 'Apple', '52']);
