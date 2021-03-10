function main(input)
{
    let type =  input[0];
    let rows = Number(input[1]);
    let columns = Number(input[2]);

    let totalSeats = rows * columns;
    let ticketPrice;
    switch (type)
    {
        case 'Premiere':
            ticketPrice = 12;
            break;
        case 'Normal':
            ticketPrice = 7.50;
            break;
        case 'Discount':
            ticketPrice = 5.00;
            break;
    }

    console.log(`${(ticketPrice * totalSeats).toFixed(2)} leva`);

}
