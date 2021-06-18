function getDay(day) {
    let days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
    ];

    let result = days[day - 1];
    console.log(typeof(result) == 'undefined' ? 'Invalid day!' : result);
}

getDay(12);
