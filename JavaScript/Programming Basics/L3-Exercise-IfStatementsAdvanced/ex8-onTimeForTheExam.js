function main(input)
{
    let hourExam = Number(input[0]);
    let minutesExam = Number(input[1]);
    let hourArrive = Number(input[2]);
    let minutesArrive = Number(input[3]);

    let totalExam = hourExam * 60 + minutesExam;
    let totalArrive = hourArrive * 60 + minutesArrive;

    let resultArrived;
    let resultTime = '';

    let diff = totalExam - totalArrive;
    let diffHours = Math.trunc(diff / 60);
    let diffMinutes = Math.trunc(diff % 60);

    if (diffMinutes <= 30 && diffMinutes >= 0 && diffHours < 1)
    {
        resultArrived = 'On time';
        if (diffHours < 1 && diffMinutes > 0)
            resultTime = `${diffMinutes} minutes before the start`;
        else if (diffMinutes > 0)
            resultTime = `${diffHours}:${diffMinutes < 10 ? '0' + diffMinutes : diffMinutes} hours before the start`;
    }

    else if (diffMinutes > 30 || diffHours >= 1)
    {
        resultArrived = 'Early';
        if (diffHours < 1)
            resultTime = `${diffMinutes} minutes before the start`;
        else
            resultTime = `${diffHours}:${diffMinutes < 10 ? '0' + diffMinutes : diffMinutes} hours before the start`;
    }

    else
    {
        diffHours = Math.abs(diffHours);
        diffMinutes = Math.abs(diffMinutes);
        resultArrived = 'Late';
        if (diffHours < 1)
            resultTime = `${diffMinutes} minutes after the start`;
        else
            resultTime = `${diffHours}:${diffMinutes < 10 ? '0' + diffMinutes : diffMinutes} hours after the start`;
    }
    
    console.log(resultArrived);
    console.log(resultTime);

} 

main(["10",
"00",
"10",
"00"]);