function circleArea(radius) {
    let argumentType = typeof(radius);
    if (argumentType != 'number') {
        console.log(`We can not calculate the circle area, because we receive a ${argumentType}.`);
        return;
    }    

    let area = radius ** 2 * Math.PI;
    console.log(area.toFixed(2));
}

circleArea('2');
circleArea([]);
circleArea(5);
circleArea(2.2);
circleArea({});
