function passwordGenerator(input) {
    const vowels = [
        'a',
        'e',
        'i',
        'o',
        'u',
    ];

    const [firstStr, secondStr, lastStr] = input;
    const concatenatedStr = firstStr + secondStr;
    const newStr = [];

    let index = 0;

    for (const symbol of concatenatedStr) {
        if (vowels.includes(symbol)) {
            const vowel = lastStr[index].toUpperCase();
            newStr.push(vowel);
            index = index == lastStr.length - 1 ? 0 : index + 1;
        } else {
            newStr.push(symbol);
        }
    }

    console.log(`Your generated password is ${newStr.reverse().join('')}`);
}

passwordGenerator([
    'ilovepizza', 
    'ihatevegetables',
    'orange'
])
