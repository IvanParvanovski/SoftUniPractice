function wordOccurrences(words) {
    let wordCount = new Map();

    for (let word of words) {
        if (!wordCount.has(word)) {
            wordCount.set(word, 0);
        }

        wordCount.set(word, wordCount.get(word) + 1);
    }

    let sortedWordCount = [...wordCount.entries()].sort((a, b) => b[1] - a[1]);

    for (let [word, count] of sortedWordCount) {
        console.log(`${word} -> ${count} times`);
    }
}

wordOccurrences([
    'Here', 'is', 'the', 'first', 'sentence', 
    'Here', 'is', 'another', 'sentence', 
    'And', 'finally', 'the', 'third', 'sentence'
]);
