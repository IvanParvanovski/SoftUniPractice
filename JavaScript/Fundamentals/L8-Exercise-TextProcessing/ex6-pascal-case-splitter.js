function pascalCaseSplitter(text) {
    function isUpper(letter) {
        return letter.toUpperCase() == letter;
    }

    let startIndex = -1;
    let splitedWords = [];

    for (let i = 0; i < text.length; i++) {
        let currentLetter = text[i];
        let isEnd = text.length - 1 == i; 

        if (isUpper(currentLetter)) {
            if (startIndex != i && startIndex != -1) {
                splitedWords.push(text.substring(startIndex, i));
            }

            startIndex = i;                
        }

        if (isEnd) {
            splitedWords.push(text.substring(startIndex, i + 1));
        }
    }

    console.log(splitedWords.join(', '));
}

pascalCaseSplitter('split');
