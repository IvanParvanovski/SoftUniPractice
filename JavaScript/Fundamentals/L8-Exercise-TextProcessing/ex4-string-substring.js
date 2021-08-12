function stringSubstring(searchedWord, text) {
    let words = text.split(' ');
    let searchedWordLowered = searchedWord.toLowerCase();

    let found = false;
    for (let word of words) {
        if (word.toLowerCase() == searchedWordLowered) {
            found = true;
            break;
        }
    }
    
    let message;
    if (found) {
        message = searchedWord;
    } else {
        message = `${searchedWord} not found!`;
    }

    console.log(message);
}

stringSubstring('javascript', 'JavaScriptA is the best programming language');
