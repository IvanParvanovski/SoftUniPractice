function getFibonator() {
    const sequence = [0, 1];

    function nextNum() {
        const sequenceLen = sequence.length;
        const result = sequence[sequence.length - 1];
        sequence.push(sequence[sequenceLen - 2] + sequence[sequenceLen - 1]);
       
        return result;
    }

    return nextNum;
}

// function getFibonator() {
//     let n1 = 0;
//     let n2 = 1;

//     function nextNum() {
//         let nextNum = n1 + n2;
//         n1 = n2;
//         n2 = nextNum;
//         return nextNum;
//     }

//     return nextNum;
// }

let fib = getFibonator();
console.log(fib());
console.log(fib());
console.log(fib());
console.log(fib());
console.log(fib());