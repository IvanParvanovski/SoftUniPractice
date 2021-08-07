function wordsTracker(words) {
    let searchedWords = words.shift().split(' ');
    let wordsOccurences = {};
    
    for (let searchedWord of searchedWords) {
        wordsOccurences[searchedWord] = 0; 
    }

    for (let word of words) {
        if (word in wordsOccurences) {
            wordsOccurences[word] += 1;
        }
    }

    let sortedWordsOccurences = Object.entries(wordsOccurences).sort((a, b) => b[1] - a[1])
    
    for (let [word, count] of sortedWordsOccurences) {
        console.log(`${word} - ${count}`);
    }
}

wordsTracker([
    'this sentence hi',
    'In', 'this', 'sentence', 'you', 'have', 'to', 'count',
    'the', 'occurances', 'of', 'the', 'words', 'this', 'and', 'sentence',
    'because', 'this', 'is', 'your', 'task'
]);
