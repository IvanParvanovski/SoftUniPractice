function furniture(input) {
    const regexPattern = />>(?<name>\w+)<<(?<price>\d+(?:.\d+)?)!(?<quantity>\d+)/;
    
    let totalMoney = 0;
    let furniture = []; 

    for (const word of input) {
        if (word == 'Purchase') {
            break;
        }

        const result = regexPattern.exec(word);

        if (!result) {
            continue;
        }

        const name = result.groups['name'];
        const price = Number(result.groups['price']);
        const quantity = Number(result.groups['quantity']);

        totalMoney += price * quantity;
        furniture.push(name);
    }

    console.log('Bought furniture:');
    console.log(furniture.join('\n'));
    console.log(`Total money spend: ${totalMoney.toFixed(2)}`);
}

furniture([
    ">>Sofa<<312.23!3",
    ">>TV<<300!5",
    ">Invalid<<!5",
    "Purchase"
]);
