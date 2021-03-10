function main(input)
{
    let holidayDays = Number(input[0]);
    let roomType = input[1];
    let grade = input[2];

    let roomPrice;
    let discount = 0;

    switch (roomType)
    {
        case 'room for one person':
            roomPrice = 18;
            break;
        
        case 'apartment':
            roomPrice = 25;
            break;
        
        case 'president apartment':
            roomPrice = 35;
            break;
    }

    let total = (holidayDays - 1) * roomPrice;

    switch (roomType) 
    {
        case 'apartment':
            if (holidayDays < 10)
                discount = 30;
            else if (holidayDays < 15)
                discount = 35;
            else
                discount = 50;
            break;
        
        case 'president apartment':
            if (holidayDays < 10)
                discount = 10;
            else if (holidayDays < 15)
                discount = 15;
            else
                discount = 20;
            break;
    }

    total -= discount / 100 * total;

    if (grade == 'positive')
        total += 0.25 * total;
    else if (grade == 'negative')
        total -= 0.10 * total;

    console.log(total.toFixed(2));
} 

main(['14', 'apartment', 'positive']);
main(['30', 'president apartment', 'negative']);
main(['12', 'room for one person', 'positive']);
main(['2', 'apartment', 'positive']);

