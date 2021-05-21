function theatre(status, age) {
    let ticketPrice;

    if (0 <= age && age <= 18) {
        switch(status) {
            case 'Weekday':
                ticketPrice = 12;
                break;
            case 'Weekend':
                ticketPrice = 15;
                break;
            case 'Holiday':
                ticketPrice = 5;
                break;
            default:
                ticketPrice = 'Error!';
                break;
        }
    } else if (18 < age && age <= 64) {
        switch(status) {
            case 'Weekday':
                ticketPrice = 18;
                break;
            case 'Weekend':
                ticketPrice = 20;
                break;
            case 'Holiday':
                ticketPrice = 12;
                break;
            default:
                ticketPrice = 'Error!';
                break;
        }
    } else if (64 < age && age <= 122) {
        switch(status) {
            case 'Weekday':
                ticketPrice = 12;
                break;
            case 'Weekend':
                ticketPrice = 15;
                break;
            case 'Holiday':
                ticketPrice = 10;
                break;
            default:
                ticketPrice = 'Error!';
                break;
        }
    } else {
        ticketPrice = 'Error!';
    }

    console.log((!isNaN(ticketPrice) ? `${ticketPrice}$`: ticketPrice));
}

theatre('Weekday', 42);
theatre('Holiday', -12);
theatre('Holiday', 15);
