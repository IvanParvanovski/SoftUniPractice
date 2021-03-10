function main(input)
{
    let locationsCount = Number(input[0]);

    let i = 1;
    while (true)
    {
        if (i >= input.length)
            break;

        let wantedGoldPerDayAverage = Number(input[i]);
        i++;

        let workingDays = Number(input[i]);
        i++;

        let totalGold = 0;
        for (let workingDay = 0; workingDay < workingDays; workingDay++)
        {
            totalGold += Number(input[i]);
            i++;
        }

        averageGold = totalGold / workingDays;

        if (averageGold >= wantedGoldPerDayAverage)
            console.log(`Good job! Average gold per day: ${averageGold.toFixed(2)}.`);
        else
            console.log(`You need ${(wantedGoldPerDayAverage - averageGold).toFixed(2)} gold.`);
    }
}
main([2,
    10,
    3,
    10,
    10,
    11,
    20,
    2,
    20,
    10,
    ])