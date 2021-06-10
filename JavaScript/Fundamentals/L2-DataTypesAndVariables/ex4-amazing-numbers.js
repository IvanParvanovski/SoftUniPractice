function isAmazing(number) {
    let numberAsString = number.toString();
    let numberSum = 0;
    
    for (let i = 0; i < numberAsString.length; i++) {
        numberSum += Number(numberAsString[i]);
    }
    
    console.log(`${number} Amazing? ${numberSum.toString().includes('9') ? 'True' : 'False'}`);
}

isAmazing(1233);