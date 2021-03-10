function main(input)
{
    let budegt = Number(input[0]);
    let season = input[1];
    let destination;
    let hut;
    let spentMoney;

    if (budegt <= 100)
    {
        destination = 'Bulgaria';
        
        switch(season)
        {
            case 'summer':
                hut = 'Camp'
                spentMoney = 0.3;
                break;
            case 'winter':
                hut = 'Hotel';
                spentMoney = 0.7;
                break;
        }
    }
    else if (budegt <= 1000)
    {
        destination = 'Balkans';
        switch(season)
        {
            case 'summer':
                hut = 'Camp';
                spentMoney = 0.4;
                break;
            case 'winter':
                hut = 'Hotel';
                spentMoney = 0.8;
                break;
        }
    }
    else
    {
        destination = 'Europe';
        hut = 'Hotel';
        spentMoney = 0.9;
    }

    console.log(`Somewhere in ${destination}`);
    console.log(`${hut} - ${(spentMoney * budegt).toFixed(2)}`);
}

main(["50", "summer"]);
