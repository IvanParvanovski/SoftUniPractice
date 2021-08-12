function repeatringChars(text) {
    let result = [];

    for (let letter of text) {
        let currentSymbol = result[result.length - 1];
        
        if (currentSymbol != letter) {
            result.push(letter);
        }
    }

    console.log(result.join(''));
}


repeatringChars('aaaabbbbbbcdddeeeedssaa');
