// function sumOfOddNumbers(number) {
//     let counter = 0;
//     let startNumber = 1;
//     let total = 0;

//     while (true) {
//         if (counter === number) {
//             break;
//         }
        
//         if (startNumber % 2 != 0) {
//             console.log(startNumber);

//             total += startNumber;
//             counter++;
//         }

//         startNumber++;    
//     }
//     console.log(`Sum: ${total}`);
// }

function sumOfOddNumbers(number) {
    let total = 0;
    for (let i = 1; number > 0; i += 2) {
        number--;
        total += i;
        console.log(i);
    }
    console.log(`Sum: ${total}`);
}

sumOfOddNumbers(5);
sumOfOddNumbers(3);
