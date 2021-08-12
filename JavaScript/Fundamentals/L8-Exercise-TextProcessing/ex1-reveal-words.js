function revealWords(words, template) {
    let wordTokens = words.split(', ');
    for (let word of wordTokens) {
        let wordAsStars = '*'.repeat(word.length);
        
        if (template.includes(wordAsStars)) {
            template = template.replace(wordAsStars, word);
        }
    }

    console.log(template);
}

// revealWords('great', 'softuni is ***** place for learning new programming languages');
revealWords('great, learning, money', 'softuni is ***** ***** place for ******** new programming languages');