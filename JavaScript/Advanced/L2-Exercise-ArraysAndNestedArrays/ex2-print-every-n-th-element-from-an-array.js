function filterTheNumbers(array, step) {
    let result = [];
    for (let i = 0; i < array.length; i += step) {
        result.push(array[i]);
    }
    return result;

    // return array.filter((x, i) => i % step == 0);
}

console.log(filterTheNumbers([5, 20, 31, 4, 20], 2));
console.log(filterTheNumbers(['1', 
'2',
'3', 
'4', 
'5'], 
6
));
