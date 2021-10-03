function carFactory(carSpecs) {
    const engines = {
        monsterEngine: {
            power: 200,
            volume: 3500,
        }, 

        normalEngine: {
            power: 120,
            volume: 2400,
        },

        smallEngine: {
            power: 90,
            volume: 1800,
        },
    }; 

    const carriageTypes = {
        hatchback: {
            type: 'hatchback',
            color: carSpecs.color,
        },

        coupe: {
            type: 'coupe',
            color: carSpecs.color,
        },
    };

    let carEngine;
    for (const engine of Object.entries(engines)) {
        if (carSpecs.power <= engine[1].power) {
            carEngine = engine[1]; 
        }
    }

    const carriage = carriageTypes[carSpecs.carriage];

    let wheelSize;
    if (carSpecs.wheelsize % 2 == 0) {
        wheelSize = Number(carSpecs.wheelsize) - 1;
    } else {
        wheelSize = Number(carSpecs.wheelsize);
    }

    let wheels = [0, 0, 0, 0].fill(wheelSize, 0, 4);

    let car = {
        model: carSpecs.model,
        engine: carEngine,
        carriage,
        wheels,
    }

    return car;
}

console.log(carFactory({ model: 'VW Golf II',
power: 90,
color: 'blue',
carriage: 'hatchback',
wheelsize: 14 }
));


console.log(carFactory({ model: 'Opel Vectra',
power: 110,
color: 'grey',
carriage: 'coupe',
wheelsize: 17 }
));
