function shop(input) {
    let pattern = />>(?<name>[A-Za-z]+)<<(?<price>\d+(?:\.\d+)?)!(?<quantity>\d+)/;
    let boughtFurniture = [];
    let total = 0;    

    for (let furniture of input) {
        if (furniture == 'Purchase') {
            break;
        }

        let match = pattern.exec(furniture);
        if (match != null) {
            boughtFurniture.push(match.groups.name);
            total += Number(match.groups.price) * Number(match.groups.quantity);
        }
    }

    console.log('Bought furniture:');
    for (let item of boughtFurniture) {
        console.log(item);
    }
    console.log(`Total money spend: ${total.toFixed(2)}`);
}

shop(['>>Sofa<<312.23!3', '>>TV<<300!5', '>Invalid<<!5', 'Purchase']);
