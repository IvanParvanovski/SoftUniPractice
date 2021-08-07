function oddOccurrences(input) {
    let words = input.split(' ');
    let wordsCount = new Map();

    for (let word of words) {
        let wordToLower = word.toLowerCase();
        
        if (!wordsCount.has(wordToLower)) {
            wordsCount.set(wordToLower, 0);
        }

        wordsCount.set(wordToLower, wordsCount.get(wordToLower) + 1);
    }

    let oddOccurrences = [...wordsCount.entries()].filter(x => x[1] % 2 != 0);    
    
    let result = []
    oddOccurrences.forEach(element => result.push(element[0]));
    
    console.log(result.join(' '));
}

oddOccurrences(
    'Java C# Php PHP Java PhP 3 C# 3 1 5 C#'
);
