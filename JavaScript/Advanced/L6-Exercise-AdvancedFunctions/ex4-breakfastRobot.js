function solution() {
    function restock(microelement, quantity) {
        this[microelement] += Number(quantity);
        return 'Success';
    }

    function prepare(recipe, productQuantity) {
        const substractedElements = {};

        for (const neededElement of Object.entries(recipes[recipe])) {
            const [name, microelementQuantity] = neededElement;
            const neededQuantity = microelementQuantity * productQuantity
            
            if (this[name] < neededQuantity || !(name in this)) {
                Object.entries(substractedElements).forEach((e) => this[e[0]] += e[1]);
                return `Error: not enough ${name} in stock`
            }

            this[name] -= neededQuantity;
            substractedElements[name] = neededQuantity;
        }

        return 'Success';
    }

    function report() {
        return `protein=${this.protein} ` +
         `carbohydrate=${this.carbohydrate} ` +
         `fat=${this.fat} ` +
         `flavour=${this.flavour} `;
    }

    function operation(input) {
        const commandTokens = input.split(' ');
        const command = commandTokens.shift();
        return commands[command](...commandTokens);
    }

    const stock = {
        protein: 0, carbohydrate: 0, fat: 0, flavour: 0,
    };

    const recipes = {
        apple: { carbohydrate: 1, flavour: 2, },
        lemonade: { carbohydrate: 10, flavour: 20, },
        burger: { carbohydrate: 5, fat: 7, flavour: 3, },
        eggs: { protein: 5, fat: 1, flavour: 1, },
        turkey: { protein: 10, carbohydrate: 10, fat: 10, flavour: 10, },
    }

    const commands = {
        restock: restock.bind(stock),
        prepare: prepare.bind(stock),
        report: report.bind(stock),
    }

    return operation; 
}



let manager = solution(); 
console.log(manager("restock flavour 50")); // Success 
console.log(manager("prepare lemonade 4 ")); // Error: not enough carbohydrate in stock 
console.log(manager("restock carbohydrate 10")); // Success 
console.log(manager("restock flavour 10")); // Success 
console.log(manager("prepare apple 1")); // Success
console.log(manager("restock fat 10")); // Success
console.log(manager("prepare burger 1")); // Success
console.log(manager("report")); // protein=0 carbohydrate=4 fat=3 flavour=55


// console.log(manager('prepare turkey 1'));
// console.log(manager('restock protein 10'));
// console.log(manager('prepare turkey 1'));
// console.log(manager('restock carbohydrate 10'));
// console.log(manager('prepare turkey 1'));
// console.log(manager('restock fat 10'));
// console.log(manager('prepare turkey 1'));
// console.log(manager('restock flavour 10'));
// console.log(manager('prepare turkey 1'));
// console.log(manager('report'));