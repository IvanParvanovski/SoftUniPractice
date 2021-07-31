function meetings(data) {
    let schedule = new Map();

    for (let plan of data) {
        let planData = plan.split(' ');

        let weekday = planData[0];
        let personName = planData[1];

        if (!schedule.has(weekday)) {
            schedule.set(weekday, personName);
            console.log(`Scheduled for ${weekday}`);
        } else {
            console.log(`Conflict on ${weekday}!`);
        }
    }
    
    for (let day of schedule) {
        console.log(`${day[0]} -> ${day[1]}`);
    }
}

meetings([
    'Monday Peter',
    'Wednesday Bill',
    'Monday Tim',
    'Friday Tim',
]);
