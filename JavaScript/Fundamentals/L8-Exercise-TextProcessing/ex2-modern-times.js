function modernTimes(input) {
    function isLetter(symbol) {
        return (symbol >= 'a' && symbol <= 'z') || 
            (symbol >= 'A' && symbol <= 'Z');
    }
    
    let words = [];
    let sentenceTokens = input.split(' ');

    for (let word of sentenceTokens) {
        if (word[0] == '#') {
            let shouldAdd = true;
            word = word.replace('#', '');

            for (let currentChar of word) {                
                if (!isLetter(currentChar)) {
                    shouldAdd = false;
                    break;
                }    
            }

            if (shouldAdd && word.length > 1) {
                words.push(word);
            }
        }
    }

    console.log(words.join('\n'));
}