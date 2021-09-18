function wordUppercase(text) {
    let pattern = /\w+/g;
    let upperCaseWords = text.match(pattern).map(x => x.toUpperCase());
    console.log(upperCaseWords.join(', '));
}

wordUppercase('Hi, how are you doing?');
