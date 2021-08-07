function cardGame(input) {
    let cardsPower = {
        2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,
        J: 11,
        Q: 12,
        K: 13,
        A: 14,
    };

    let multipliers = {
        S: 4,
        H: 3,
        D: 2,
        C: 1
    }

    let players = [];

    for (let personData of input) {
        let [person, deckData] = personData.split(': ');
        let deck = deckData.split(', ');

        let searchedPlayer = players.find(x => x.name == person);
        let player;

        if (!searchedPlayer) {
            player = {
                name: person,
                cards: [],
                total: 0,
            };
        } else {
            player = searchedPlayer;
        }

        let currentSum = 0;
        for (let card of deck) {
            if (!player.cards.includes(card)) {
                let cardPower;
                let cardMultiplier;

                if (card[0] == '1' && card[1] == '0') {
                    cardPower = cardsPower[10];
                    cardMultiplier = multipliers[card[2]]
                } else {
                    cardPower = cardsPower[card[0]];
                    cardMultiplier = multipliers[card[1]];
                }
    
                currentSum += cardPower * cardMultiplier;
                player.cards.push(card);
            }
        }

        player.total += currentSum;
        
        if (!searchedPlayer) {
            players.push(player);
        }
    }

    for (let player of players) {
        console.log(`${player.name}: ${player.total}`);
    }
}
cardGame([
    'Peter: 2C, 4H, 9H, AS, QS',
    'Tomas: 3H, 10S, JC, KD, 5S, 10S',
    'Andrea: QH, QC, QS, QD',
    'Tomas: 6H, 7S, KC, KD, 5S, 10C',
    'Andrea: QH, QC, JS, JD, JC',
    'Peter: JD, JD, JD, JD, JD, JD', 
]);
