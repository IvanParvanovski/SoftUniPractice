function recordTemps(daysRecords, weekRecords) {
    let result = [];
    for (let i = 0; i < daysRecords.length; i++) {
        let currentDay = daysRecords[i];
        let currentWeekDay = weekRecords[i];

        let lowVal;
        let highVal;

        if (currentDay[0] < currentWeekDay[0]) {
            lowVal = currentDay[0];
        } else {
            lowVal = currentWeekDay[0];
        }

        if (currentDay[1] > currentWeekDay[1]) {
            highVal = currentDay[1];
        } else {
            highVal = currentWeekDay[1];
        }

        result.push([lowVal, highVal]);
    }

    return result;
}

console.log(recordTemps(
    [[34, 82], [24, 82], [20, 89], [5, 88], [9, 88], [26, 89], [27, 83]],
    [[44, 72], [19, 70], [40, 69], [39, 68], [33, 64], [36, 70], [38, 69]]
));
