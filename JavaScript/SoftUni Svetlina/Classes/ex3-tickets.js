function main(ticketsData, criteria) {
    class Ticket {
        constructor(destination, price, status) {
            this.destination = destination;
            this.price = price;
            this.status = status;
        }
    }

    const tickets = [];

    for (const t of ticketsData) {
        const [destination, price, status] = [...t.split('|')];
        const tempTicket = new Ticket(destination, price, status);
        tickets.push(tempTicket);
    }


    const sortedTickets = tickets.sort((a, b) => {
        if (typeof(a[criteria]) == 'string') {
            return b[criteria].localeCompare(a[criteria]);
        }
        return b[criteria] - a[criteria];
    })

    return sortedTickets;
}


// let asd = [
//     {'fruit': 'orange', 'quantity': 1}, 
//     {'fruit': 'apple', 'quantity': 2}
// ];

// let criteria = 'fruit';
// console.log(typeof asd[0][criteria])


console.log(main(
    ['Philadelphia|94.20|available',
        'New York City|95.99|available',
        'New York City|95.99|sold',
        'Boston|126.20|departed'
    ],
    'destination'
));
