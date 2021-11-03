function dayOfWeek(day) {
    const days = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    ];

    let result = days.indexOf(day);

    if (result == -1) {
        console.log('error');
    } else {
        console.log(result + 1);
    }
}

dayOfWeek('Monday');
dayOfWeek(2);
dayOfWeek(3);
dayOfWeek(4);
dayOfWeek(5);
dayOfWeek(6);
dayOfWeek(7);
dayOfWeek('Invalid');
