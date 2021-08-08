function censoreWords(text, searchedWord) {
    while (text.includes(searchedWord)) {
        text = text.replace(searchedWord, '*'.repeat(searchedWord.length));
    }
    
    console.log(text);
}

censoreWords('A small sentence with some words', 'small');
censoreWords('A ** sentence with some words **', '**');
