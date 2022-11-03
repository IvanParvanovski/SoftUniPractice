function main(text) {
    const words = text.split(' ');
    const result = [];
    let longestWord = 0;

    for (const word of words) {
        const reversedWord = [...word].reverse().join('');
        const reversedWordLength = reversedWord.length;

        if (reversedWordLength > longestWord) {
            longestWord = reversedWordLength;
        }

        result.push(reversedWord)
    }

    for (let i = 0; i < result.length; i++) {
        const word = result[i];
        const spaces = ' '.repeat(longestWord + 1 - word.length)

        result[i] = `* ${word}${spaces}*`;

    }

    const border = '*'.repeat(longestWord + 4);
    result.unshift(border);
    result.push(border);
    
    return result.join('\n');
}

console.log(main('My spicy world is great'));
console.log(main('Hello World'));

moveWords('ivan')