function reverseAndCut(text) {
    let middle = parseInt(text.length / 2);
    
    let [firstPart, secondPart] = [
        text.substring(0, middle),
        text.substring(middle),
    ];

    console.log([...firstPart].reverse().join(''));    
    console.log([...secondPart].reverse().join(''));    
}

reverseAndCut(
    'Hel',
);

reverseAndCut('Helo');
