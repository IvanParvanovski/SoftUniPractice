function train(input) {
    let wagons = input.shift().split(' ').map(x => Number(x));
    let wagonMax = Number(input.shift());

    while (input.length > 0) {
        let commandData = input.shift().split(' ');
        let command = commandData[0];
        
        if (command == 'Add') {
            let passengers = Number(commandData[1]);
            wagons.push(passengers);
        } else {
            let passengers = Number(command);

            for (let i = 0; i < wagons.length; i++) {
                let currentPassengers = wagons[i];

                if (currentPassengers + passengers <= wagonMax) {
                    wagons[i] += passengers;
                    break;
                }
            }
        }
    }
    console.log(wagons.join(' '));
}

train([
    '32 54 21 12 4 0 23',
    '75',
    'Add 10',
    'Add 0',
    '30',
    '10',
    '75'
]);