function main(input)
{
    let town = input[0];
    let trades = Number(input[1]);
    let commission;

    switch (town)
    {
        case 'Sofia':
            if (0 <= trades && trades <= 500)
                commission = 5;
            else if (500 < trades && trades <= 1000)
                commission = 7;
            else if (1000 < trades && trades <= 10000)
                commission = 8;
            else if (trades > 10000)
                commission = 12;

            break;
        case 'Varna':
            if (0 <= trades && trades <= 500)
                commission = 4.5;
            else if (500 < trades && trades <= 1000)
                commission = 7.5;
            else if (1000 < trades && trades <= 10000)
                commission = 10;
            else if (trades > 10000)
                commission = 13;
            break;

        case 'Plovdiv':
            if (0 <= trades && trades <= 500)
                commission = 5.5;
            else if (500 < trades && trades <= 1000)
                commission = 8;
            else if (1000 < trades && trades <= 10000)
                commission = 12;
            else if (trades > 10000)
                commission = 14.5;
            break;
    }
    console.log(!isNaN(commission) ? (commission / 100 * trades).toFixed(2) : 'error');
}

main(['Plovdiv', '-20']);