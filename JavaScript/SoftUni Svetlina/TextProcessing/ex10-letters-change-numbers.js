function lettersChangeNumbers(text) {
    const regexPattern = /(?<startLetter>[A-Za-z])(?<number>\d+)(?<lastLetter>[A-Za-z])/;
    const words = text.split(/\s+/);
    let totalSum = 0;
    
    for (const word of words) {
        const match = regexPattern.exec(word);
        
        if (!match) {
            continue;
        }

        const firstLetter = match.groups.startLetter;
        const lastLetter = match.groups.lastLetter;
        let number = Number(match.groups.number);

        if (firstLetter >= 'A' && firstLetter <= 'Z') {
            number /= firstLetter.charCodeAt(0) - 64;
        } else if (firstLetter >= 'a' && firstLetter <= 'z') {
            number *= firstLetter.charCodeAt(0) - 96;
        }

        if (lastLetter >= 'a' && lastLetter <= 'z') {
            number += lastLetter.charCodeAt(0) - 96;
        } else if (lastLetter >= 'A' && lastLetter <= 'Z') {
            number -= lastLetter.charCodeAt(0) - 64;
        }

        totalSum += number;
    }

    console.log(totalSum.toFixed(2));
}

lettersChangeNumbers('A12b s17G');
lettersChangeNumbers('P34562Z q2576f   H456z');
lettersChangeNumbers('a1A');
