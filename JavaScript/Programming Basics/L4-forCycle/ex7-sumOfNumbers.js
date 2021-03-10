
// WRONG !!!

// function main(input)
// {
//     // READ IT WRONG
//     // Right: 56489132423467788001
//     // Wrong: 56489132423467788000
//     let number = Number(input[0]); 
//     let total = 0;
//     while (number > 0)
//     {
//         total += number % 10;
//         number /= 10;
//         number = parseInt(number);
//     }

//     console.log(`The sum of the digits is:${total}`);
// }

// main(['56489132423467788001']);

function main(input)
{
    let number = input[0];
    let total = 0;
    
    for (let i = 0; i < number.length; i++)
        total += Number(number.charAt(i));
    
    console.log(`The sum of the digits is:${total}`);
}