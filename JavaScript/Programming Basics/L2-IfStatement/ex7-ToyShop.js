function main (input)
{
    let holidayPrice = Number(input[0]);
    
    let puzzles = Number(input[1]);
    let dols = Number(input[2]);
    let bears = Number(input[3]);
    let minions = Number(input[4]);
    let trucks = Number(input[5]);

    let puzzlesCost = puzzles * 2.60;
    let dolsCost = dols * 3;
    let bearsCost = bears * 4.10;
    let minionsCost = minions * 8.20;
    let trucksCost = trucks * 2;

    let totalToys = puzzles + dols + bears + trucks + minions;
    let total = puzzlesCost + dolsCost + bearsCost + minionsCost + trucksCost;
    
    if (totalToys >= 50)
        total -= 0.25 * total;

    total -= 0.1 * total;

    if (total >= holidayPrice)
        console.log(`Yes! ${(total - holidayPrice).toFixed(2)} lv left.`);
    else
        console.log(`Not enough money! ${(holidayPrice - total).toFixed(2)} lv needed.`);
}

// main(['40.8', '20', '25', '30', '50', '10']);
