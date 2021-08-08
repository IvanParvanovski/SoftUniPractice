function countStringOccurrences(text, word) {
    let count = 0;
    word = ` ${word} `;
    text = ` ${text} `;
    
    let index = text.indexOf(word);
    while (index != -1) {
        count++;
        index = text.indexOf(word, index + 1);
    }

    console.log(count);
}

function countStringOccurences(text, word) {
    return ` ${text} `.split( `${word} `).length - 1;
}

countStringOccurrences('This is, is a word and it also is a sentence is', 'is');

