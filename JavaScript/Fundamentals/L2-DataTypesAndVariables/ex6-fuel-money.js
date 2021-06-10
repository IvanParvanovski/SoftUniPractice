function neededFuel(distance, passengers, price) {
    let consumption = 7 + passengers * 0.1;
    let fuel = distance / 100 * consumption;
    const total = fuel * price;
    console.log(`Needed money for that trip is ${total.toFixed(2)}lv.`);
}

console.log(neededFuel(260, 9, 2.49));
