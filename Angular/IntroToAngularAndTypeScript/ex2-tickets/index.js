var Ticket = /** @class */ (function () {
    function Ticket(destination, price, status) {
        this.destination = destination;
        this.price = price;
        this.status = status;
    }
    return Ticket;
}());
function main(input, secondCriterion) {
    var tickets = [];
    for (var _i = 0, input_1 = input; _i < input_1.length; _i++) {
        var ticket = input_1[_i];
        var _a = ticket.split('|'), destination = _a[0], price = _a[1], status_1 = _a[2];
        tickets.push(new Ticket(destination, price, status_1));
    }
    if (secondCriterion == 'price') {
        return tickets.sort(function (a, b) { return Number(a[secondCriterion]) - Number(b[secondCriterion]); });
    }
    return tickets.sort(function (a, b) { return a[secondCriterion].localeCompare(b[secondCriterion]); });
}
console.log(main([
    'Philadelphia|94.20|available',
    'New York City|95.99|available',
    'New York City|95.99|sold',
    'Boston|126.20|departed'
], 'destination'));
// main([
//     'Philadelphia|94.20|available',
//     'New York City|95.99|available',
//     'New York City|95.99|sold',
//     'Boston|126.20|departed'
//     ],
//     'status');
