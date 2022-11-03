function main(inputStr) {
    const words = inputStr.split(' ');
    const result = [];

    for (const word of words) {
        let leftSide = [];
        let rightSide = [];
    
        let middle = Math.round(word.length / 2);
        
        for (let i = 0; i < middle; i++) {
            leftSide.push(word[i]);
        }
    
        for (let i = middle; i < word.length; i++) {
            rightSide.push(word[i]);
        }
    
        let leftChar = '';
        if (word.length % 2 != 0) {
            leftChar = leftSide.pop();
        }

        result.push(
            `${leftSide.reverse().join('')}${leftChar}${rightSide.reverse().join('')}`
        );
    }
   
    console.log(result.join(' '));
}

main('taxi');
main('taxis');
main('man i need a taxi up to ubud')
