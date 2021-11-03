function fruit(fruit, weight, price) {
    const kilos = Number(weight) / 1000;
    const result = kilos * Number(price);

    console.log(`I need $${result.toFixed(2)} to buy ${kilos.toFixed(2)} kilograms ${fruit}.`);
}

fruit('orange', 2500, 1.80);