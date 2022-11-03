function piccolo(inputArray) {
    const parking = {};

    for (const carInfo of inputArray) {
        const [status, number] = carInfo.split(', ');
        parking[number] = status;
    }

    const cars = Object.entries(parking).filter(x => x[1] == 'IN');

    if (Object.keys(cars).length == 0) {
        console.log('Parking Lot is Empty');
    } else {
        const res = cars.sort((a, b) => a[0].localeCompare(b[0]));
            
        for (const r of res) {
            console.log(r[0]);
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
'IN, CA2822UU']);

// piccolo(['IN, CA2844AA',
// 'IN, CA1234TA',
// 'OUT, CA2844AA',
// 'OUT, CA1234TA']);