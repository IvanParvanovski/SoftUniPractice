function cookingByNumbers(number,
    firstOpr,
    secondOpr,
    thirdOpr,
    forthOpr,
    fifthOpr) {
    
    number = Number(number);

    let operations = {
        'chop': (num) => num / 2,
        'dice': (num) => Math.sqrt(num),
        'spice': (num) => num + 1,
        'bake': (num) => num * 3,
        'fillet': (num) => num - (0.2 * num),
    }

    let operationArray = [firstOpr, secondOpr, thirdOpr, forthOpr, fifthOpr];

    let result = number;
    for (let opr of operationArray) {
        result = operations[opr](result);
        console.log(result);
    }
}

cookingByNumbers(32, 'chop', 'chop', 'chop', 'chop', 'chop');
cookingByNumbers('9', 'dice', 'spice', 'chop', 'bake', 'fillet');