function solve(input) {
    let availableCards = input.shift().split(':');
    let cards = [];

    for (let commandData of input) {
        let commandTokens = commandData.split(' ');
        let command = commandTokens[0];
        
        if (command == 'Ready') {
            break;
        }

        let cardName = commandTokens[1];

        switch (command) {
            case 'Add':
                if (availableCards.includes(cardName)) {
                    cards.push(cardName);
                } else {
                    console.log('Card not found.');
                }
                break;

            case 'Insert':
                let index = Number(commandTokens[2]);
                
                if (availableCards.includes(cardName) && index < cards.length && index > -1) {
                    cards.splice(index, 0, cardName);
                } else {
                    console.log('Error!');
                }
                break;

            case 'Remove':
                if (cards.includes(cardName)) {
                    cards.splice(cards.indexOf(cardName), 1);
                } else {
                    console.log('Card not found.');
                }
                break;

            case 'Swap':
                let secondCardName = commandTokens[2];

                let firstCardIndex = cards.indexOf(cardName);
                let secondCardIndex = cards.indexOf(secondCardName);
                let firstCard = cards[firstCardIndex];

                cards[firstCardIndex] = cards[secondCardIndex];
                cards[secondCardIndex] = firstCard;
                break;

            case 'Shuffle':
                cards = cards.reverse();
                break;
        }
    }
    console.log(cards.join(' '));
}   

solve(["Innervate:Moonfire:Pounce:Claw:Wrath:Bite",
"Add Moonfire",
"Add Pounce",
"Add Bite",
"Add Wrath",
"Insert Claw 0",
"Swap Claw Moonfire",
"Remove Bite",
"Shuffle deck",
"Ready"]);
