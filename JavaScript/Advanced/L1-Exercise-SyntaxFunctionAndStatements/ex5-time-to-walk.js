function timeToWalk(steps, stepLength, speed) {    
    // 4000 steps
    // 0.60 meters per step
    // S = 4000 * 0.60 = 2400 meters
    // V = 5 km/h * 5/18 = 1.3 m/s
    // T = S / V = 2400 / 1.3 = 1800 s
    // 1800 = 30.76 min
    // +T = 2400 / 500 = 4 more minutes


    let distanceInMeters = steps * stepLength;
    let speedInMeterPerSecond = speed * 5/18;

    let addedSeconds = parseInt(distanceInMeters / 500) * 60;
    let timeInSeconds = distanceInMeters / speedInMeterPerSecond + addedSeconds;
    
    let minutes = parseInt(timeInSeconds / 60);
    let leftSeconds = Math.round(timeInSeconds % 60);

    let hours = parseInt(minutes / 60);
    let leftMinutes = Math.round(minutes % 60);

    let hoursWithLeadingZeros = hours.toString().padStart(2, '0');
    let minutesWithLeadingZeros = leftMinutes.toString().padStart(2, '0');
    let secondsWithLeadingZeros= leftSeconds.toString().padStart(2, '0');

    console.log(`${hoursWithLeadingZeros}:${minutesWithLeadingZeros}:${secondsWithLeadingZeros}`);
}

timeToWalk(4000, 0.60, 5);
timeToWalk(2564, 0.70, 5.5);
