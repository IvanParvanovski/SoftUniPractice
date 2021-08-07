function numberPlateRecognition(input) {
    let hotelCars = []; 

    for (let numberPlateData of input) {
        let [numberPlateStatus, numberPlate] = numberPlateData.split(', ');

        if (numberPlateStatus == 'IN') {
            if (!hotelCars.includes(numberPlate)) {
                hotelCars.push(numberPlate);
            }
        } else {
            if (hotelCars.includes(numberPlate)) {
                hotelCars.splice(hotelCars.indexOf(numberPlate), 1);
            }
        }
    }

    if (hotelCars.length == 0) {
        console.log('Parking Lot is Empty');
    } else {
        let hotelCarsSorted = hotelCars.sort((a, b) => {
            return a.localeCompare(b);
        })

        console.log(hotelCarsSorted.join('\n'))
    }
}

numberPlateRecognition(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'IN, CA9999TT',
'IN, CA2866HI',
'OUT, CA1234TA',
'IN, CA2844AA',
'OUT, CA2866HI',
'IN, CA9876HH',
'IN, CA2822UU']
);

// numberPlateRecognition([]);