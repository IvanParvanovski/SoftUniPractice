function replaceRepeatingChars(text) {
    const result = [];
    let lastLetter = ''; 

    for (const symbol of text) {
        if (symbol != lastLetter) {
            result.push(symbol);
            lastLetter = symbol;
        }
    }

    console.log(result.join(''));
}

replaceRepeatingChars('aaaaabbbbbcdddeeeedssaa');
replaceRepeatingChars('qqqwerqwecccwd');