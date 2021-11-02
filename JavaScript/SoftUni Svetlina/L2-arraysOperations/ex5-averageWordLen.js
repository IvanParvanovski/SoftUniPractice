function averageWordLength(sentence) {
    const matches = sentence.match(/\w+/g);
    
    // [1, 2, 3, 4] => 10
    return (matches.reduce((total, currentVal) => {
        return total + currentVal.length;
    }, 0) / matches.length).toFixed(2);    
}

console.log(averageWordLength('One upon a time .there was, a brave knight, who had a sword.'));
console.log(averageWordLength('One upon a time'));

