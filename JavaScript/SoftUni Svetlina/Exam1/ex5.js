function capToFront(text) {
    const lowerCase = [];
    const upperCase = [];

    for (const symbol of text) {
        if (symbol.toUpperCase() == symbol) {
            upperCase.push(symbol);
        } else {
            lowerCase.push(symbol);
        }
    }

    return upperCase.join('') + lowerCase.join('');
}


console.log(capToFront('hApPy'));

console.log(capToFront('moveMENT'));

console.log(capToFront('shOrtCAKE'));
