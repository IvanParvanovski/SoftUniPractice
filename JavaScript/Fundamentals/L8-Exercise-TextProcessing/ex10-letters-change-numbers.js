function mathGame(input) {
    function positionInAlphabet(letter) {
        let letterToLower = letter.toLowerCase();
        return letterToLower.charCodeAt(0) - 96;
    }

    let sequences = input.split(/\s+/);
    let total = 0;

    for (let sequence of sequences) {
        let startLetter = sequence[0];
        let endLetter = sequence[sequence.length - 1];
        let number = Number(sequence.substring(1, sequence.length - 1));
        
        if (startLetter != undefined) {
            let startLetterPosition = positionInAlphabet(startLetter);
            if (startLetter == startLetter.toUpperCase()) {
                number /= startLetterPosition;
            } else {
                number *= startLetterPosition;
            }
        }

        if (endLetter != undefined) {
            let endLetterPosition = positionInAlphabet(endLetter);
            if (endLetter == endLetter.toUpperCase()) {
                number -= endLetterPosition;            
            } else {
                number += endLetterPosition;
            }
        }
        
        total += number;
    }

    console.log(total.toFixed(2));
}

mathGame('a1A');
mathGame('A12b s17G');
mathGame('P34562Z q2576f   H456z');
mathGame('A90a');
