function main(input)
{
    let year = input[0];
    let holidays = Number(input[1]);
    let weekendsInTown = Number(input[2]);
    let weekendsInSofia = 48 - weekendsInTown;

    let gamesInSofia = weekendsInSofia * 3 / 4;
    let gamesInHolidays = holidays * 2 / 3;

    let totalGames = gamesInSofia + gamesInHolidays + weekendsInTown;
    
    if (year == 'leap')
        totalGames += totalGames * 0.15;
    
    console.log(Math.floor(totalGames));
}

main(["leap",
"5",
"2"]);