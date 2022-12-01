function hardWord(input) {
    let [text, words] = input;
    const sortedWords = words.sort((a, b) => b.length - a.length);

    for (const word of sortedWords) {
        const underscores = '_'.repeat(word.length);
    
        let position = text.indexOf(underscores);
        while (position != -1) {
            text = text.replace(underscores, word);
            position = text.indexOf(underscores);
        }    
    }

    console.log(text);
}

hardWord(
    [
        'Hi, grandma! I\'m so ____ to write to you. ______ the winter vacation, so _______ things happened. My dad bought me a sled. Mom started a new job as a __________. My brother\'s ankle is ________, and now it bothers me even more. Every night Mom cooks ___ on your recipe because it is the most delicious. I hope this year Santa will _____ me a robot.',
    
        [
            'pie', 
            'bring', 
            'glad', 
            'During', 
            'amazing', 
            'pharmacist', 
            'sprained'
        ]
    ])
