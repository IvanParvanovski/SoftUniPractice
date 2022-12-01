function revealWords(text, sentence) {
    const words = text.split(', ');

    for (const word of words.sort((a, b) => b.length - a.length)) {
        const stars = '*'.repeat(word.length);
        
        let position = sentence.indexOf(stars);
        while (position != -1) {
            sentence = sentence.replace(stars, word);

            position = sentence.indexOf(stars);
        }
    }

    console.log(sentence);
}

revealWords(
    'great',
    'softuni is ***** place for learning new programming languages')