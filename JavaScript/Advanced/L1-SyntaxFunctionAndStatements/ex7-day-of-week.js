function dayOfWeek(day) {
    let days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday', 
    ];

    let index = days.findIndex(x => x == day);
    console.log(index != -1 ? index + 1 : 'error');
}   

dayOfWeek('hi');

