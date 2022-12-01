function pascalCaseSplitter(text) {
    const words = [];
    let newWord = [];

    for (const symbol of text) {
        if (symbol >= 'A' && symbol <= 'Z' && newWord.length != 0) {
            words.push(newWord.join(''));
            newWord = [];
        }

        newWord.push(symbol);
    }

    words.push(newWord.join(''));
    console.log(words.join(', '));
}

pascalCaseSplitter('SplitMeIfYouCanHaHaYouCantOrYouCan');
pascalCaseSplitter('HoldTheDoor');
pascalCaseSplitter('ThisIsSoAnnoyingToDo');
