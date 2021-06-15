// function calculator(firstNum, operator, secondNum) {
//     let result;
//     switch(operator) {
//         case '+':
//             result = firstNum + secondNum;
//             break;
//         case '-':
//             result = firstNum - secondNum;
//             break;
//         case '*':
//             result = firstNum * secondNum;
//             break;
//         case '/':
//             result = firstNum / secondNum;
//             break;
//     }
//     console.log(result.toFixed(2));
// }

function calculator(firstNum, operator, secondNum) {
    console.log(eval(`${firstNum}${operator}${secondNum}`).toFixed(2));
}
calculator(2, '+', 2);
calculator(2, '/', 2);
calculator(2, '*', 2);
calculator(2, '-', 2);
