class Ticket {
    constructor(
        public destination: string,
        public price: string,
        public status: string
    ) {}
}

function main(input: Array<string>, secondCriterion: string) {
    const tickets: Array<Ticket> = [];
    for (const ticket of input) {
        const [destination, price, status] = ticket.split('|');
        tickets.push(new Ticket(destination, price, status));
    }

    if (secondCriterion == 'price') {
        return tickets.sort((a, b) => Number(a[secondCriterion]) - Number(b[secondCriterion]));
    }  
    return tickets.sort((a, b) => a[secondCriterion].localeCompare(b[secondCriterion]));
}

// console.log(main(
//     [
//         'Philadelphia|94.20|available',
        
//         'New York City|95.99|available',
        
//         'New York City|95.99|sold',
        
//         'Boston|126.20|departed'
        
//         ],
        
//         'destination'
// ));

console.log(main([

    'Philadelphia|94.20|available',
    
    'New York City|95.99|available',
    
    'New York City|95.99|sold',
    
    'Boston|126.20|departed'
    
    ],
    
    'status'));
