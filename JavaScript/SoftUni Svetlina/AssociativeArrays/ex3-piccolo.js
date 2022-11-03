function piccolo(inputArray) {
    const cars = {};

    for (const element of inputArray) {
        const [status, number] = element.split(', ');
        cars[number] = status;
    }

    if (Object.keys(cars).length == 0) {
        console.log('Parking Lot is Empty');
    } else {
        for (const car of Object.entries(cars).sort((a, b) => a[0].localeCompare(b[0]))) {
            if (car[1] == 'IN') {
                console.log(car[0]);
            }
        }
    }
}

piccolo(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'IN, CA9999TT',
'IN, CA2866HI',
'OUT, CA1234TA',
'IN, CA2844AA',
'OUT, CA2866HI',
'IN, CA9876HH',
'IN, CA2822UU'])