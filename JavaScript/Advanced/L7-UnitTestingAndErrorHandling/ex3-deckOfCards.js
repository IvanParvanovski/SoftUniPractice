function solve(cards) {
    function generateCard(face, suit) {
        const faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
        const suits = {
            'S': '\u2660',
            'H': '\u2665',
            'D': '\u2666',
            'C': '\u2663',
        };

        if (!(suit in suits)) {
            throw new Error(`Invalid suit ${suit}!`);
        }

        if (!(faces.includes(face))) {
            throw new Error(`Invalid face ${face}!`);
        }

        return {
            face,
            suit,
            toString() {
                return this.face + suits[suit];
            }
        }
    }

    let result = [];

    for (const card of cards) {
        let face = card.slice(0, -1);
        let suit = card.slice(-1);
        
        try {
            result.push(generateCard(face, suit).toString());
        } catch {
            console.log(`Invalid card: ${card}`);
            return;
        }
    }

    console.log(result.join(' '));
}
