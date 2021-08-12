function generatePassword(input) {
    let vowels = ['a', 'o', 'u', 'i', 'e'];

    let firstString = input[0];
    let secondString = input[1];
    let thirdString = input[2];

    let password = [];
    let concatenatedString = firstString + secondString;
    let thirdStringIndex = 0;

    for (let letter of concatenatedString) {
        if (vowels.includes(letter)) {
            if (thirdStringIndex >= thirdString.length) {
                thirdStringIndex = 0;
            }

            password.push(thirdString[thirdStringIndex].toUpperCase());   
            thirdStringIndex++; 
        } else {
            password.push(letter);
        }
    }

    console.log(`Your generated password is ${password.reverse().join('')}`);
}

generatePassword([
    'ilovepizza',
    'ihatevegetables',
    'orange'
]);
