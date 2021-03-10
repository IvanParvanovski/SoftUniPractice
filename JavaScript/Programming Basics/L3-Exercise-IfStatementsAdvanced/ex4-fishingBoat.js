function main(input)
{
    let budget = Number(input[0]);
    let season = input[1];
    let fisherMans = Number(input[2]);
    
    let boatPrice;
    switch (season)
    {
        case 'Spring':
            boatPrice = 3000;
            break;
        case 'Summer':
        case 'Autumn':
            boatPrice = 4200;
            break;
        case 'Winter':
            boatPrice = 2600;
            break;
    }
    
    let discount;
    if (fisherMans <= 6)
        discount = 0.10;
    else if (fisherMans <= 11)
        discount = 0.15;
    else
        discount = 0.25;
    
    if (fisherMans % 2 == 0 && season != 'Autumn')
        boatPrice -= 0.05 * boatPrice

    boatPrice -= discount * boatPrice;
    let diff = budget - boatPrice;

    let result;
    if (diff >= 0)
        result = `Yes! You have ${diff.toFixed(2)} leva left.`;
    else
        result = `Not enough money! You need ${Math.abs(diff).toFixed(2)} leva.`;
    
    console.log(result);
} 

main(['0',
    'Summer',
    '4']);

main(['0',
    'Summer',
    '5']);

main(['0',
    'Summer',
    '6']);

main(['0',
    'Summer',
    '7']);

main(['0',
    'Summer',
    '8']);

main(['3000',
    'Summer',
    '9']);

main(['3000',
    'Summer',
    '10']);

main(['3000',
    'Summer',
    '11']);

main(['3000',
    'Summer',
    '12']);

main(['3000',
    'Summer',
    '13']);

main(['3000',
    'Summer',
    '14']);

main(['3000',
    'Summer',
    '15']);

main(['3000',
    'Summer',
    '16']);

main(['3000',
    'Summer',
    '17']);

main(['3000',
'Summer',
'18']);