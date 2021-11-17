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

    console.log(upperCase.join('') + lowerCase.join(''));
}

capToFront('hApPy');
capToFront('moveMENT');
capToFront('shOrtCAKE');
