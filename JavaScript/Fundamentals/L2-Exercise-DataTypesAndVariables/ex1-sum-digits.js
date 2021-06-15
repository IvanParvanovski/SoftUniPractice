// function digitsSum(number) {
//     let total = 0;
//     while (number > 0) {
//         total += number % 10;
//         number = parseInt(number / 10);
//     }
    
//     console.log(total);
// }

function digitsSum(number) {
    let total = 0;
    let numberAsStr = number.toString();

    for (let digit of numberAsStr) {
        total += Number(digit)
    }

    console.log(total);
}

digitsSum(123)
// 6

digitsSum(111111111111111111111111111111);
// 30
