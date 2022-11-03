function oddOccurrences(inputVals) {
    const words = inputVals.split(' ');
    const res = {};

    for (const word of words) {
        const wordLower = word.toLowerCase();
        
        if (!(wordLower in res)) {
            res[wordLower] = 0;
        }

        res[wordLower] += 1;
    }

    const oddOccurrencesOfWords = Object.entries(res).filter(kvp => kvp[1] % 2 != 0).sort((a, b) => b[1] - a[1]);
    let resStr = '';

    for (const kvp of Object.values(oddOccurrencesOfWords)) {
        resStr += kvp[0] + ' ';
    }

    console.log(resStr);
}

oddOccurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
