function roadRadar(speed, location) {
    speed = Number(speed);

    let limits = {
        'motorway': 130,
        'interstate': 90,
        'city': 50,
        'residential': 20,
    }

    let allowedSpeed = limits[location];
    let result;

    if (speed > allowedSpeed) {
        let status;
        let diff = speed - allowedSpeed;

        if (diff <= 20) {
            status = 'speeding';
        } else if (diff <= 40) {
            status = 'excessive speeding';
        } else {
            status = 'reckless driving';
        }

        result = `The speed is ${diff} km/h faster than the allowed speed of ${allowedSpeed} - ${status}`;
    } else {
        result = `Driving ${speed} km/h in a ${allowedSpeed} zone`;
    }

    console.log(result);
}

// roadRadar(40, 'city');
// roadRadar(21, 'residential');
roadRadar(120, 'interstate');
roadRadar(200, 'motorway');