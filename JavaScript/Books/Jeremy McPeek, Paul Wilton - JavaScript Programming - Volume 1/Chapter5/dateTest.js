function main()
{
    let currentDate = new Date();
    console.log(currentDate);

    let nowHours = currentDate.getHours();
    let nowMinutes = currentDate.getMinutes();
    console.log('Current Hours: ' + nowHours);
    console.log('Current Minutes: ' + nowMinutes);

    currentDate.setHours(9);
    currentDate.setMinutes(64);
    console.log('');

    let changedHours = currentDate.getHours();
    let changedMinutes = currentDate.getMinutes();
    console.log('Changed Hours: ' + changedHours);
    console.log('Changed Minutes: ' + changedMinutes);

    console.log(currentDate);
}

main();
