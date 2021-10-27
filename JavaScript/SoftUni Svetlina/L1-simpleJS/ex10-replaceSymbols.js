function replaceSymbols(message) {
    let result = message;
    const messageArr = [...message];

    for (const letter of message) {
       
        if (messageArr.filter(x => x == letter).length == 1) {
            result = result.replace(letter, '+');
        } else {
            while (result.includes(letter)) {
                result = result.replace(letter, '=');
            }
        }
    }

    return result;
}

console.log(replaceSymbols('hello'));
