function objectFactory(library, orders) {
    return orders.map(compose);

    function compose(order) {
        // Create empty object
        // Copy properties from template
        // Compose methods from library for every item in parts
        // Return result

        const result = Object.assign({}, order.template);
        for (const func of order.parts) {
            result[func] = library[func];
        }

        return result;
    }
}

const library = {
    print: function () {
        console.log(`${this.name} is printing a page`);
    },
    scan: function () {
        console.log(`${this.name} is scanning a document`);
    },
    play: function (artist, track) {
        console.log(`${this.name} is playing '${track}' by ${artist}`);
    },
};

const orders = [
    {
        template: { name: 'ACME Printer' },
        parts: ['print']
    },
    {
        template: { name: 'Initech Scanner' },
        parts: ['scan']
    },
    {
        template: { name: 'ComTron Copier' },
        parts: ['scan', 'print']
    },
    {
        template: { name: 'BoomBox Stereo' },
        parts: ['play']
    }
];


console.log(objectFactory(library, orders));