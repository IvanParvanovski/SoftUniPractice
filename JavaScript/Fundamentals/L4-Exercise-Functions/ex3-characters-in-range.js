function charactersInRange(startChar, endChar) {
    function getStartAndEnd(startAsNum, endAsNum) {
        let start = startCharAsNum;
        let end = endCharAsNum;
    
        if (startCharAsNum > endCharAsNum) {
            start = endCharAsNum;
            end = startCharAsNum;
        } 

        return [start, end];
    }

    let startCharAsNum = startChar.charCodeAt(0);
    let endCharAsNum = endChar.charCodeAt(0)
    let result = [];
    
    let startAndEnd = getStartAndEnd(startCharAsNum, endCharAsNum);
    let start = startAndEnd[0];
    let end = startAndEnd[1];

    for (let i = start + 1; i < end; i++) {
        result.push(String.fromCharCode(i));
    }
    
    return result.join(' ');
}

console.log(charactersInRange('#', ':'));
console.log(charactersInRange('C', '#'))