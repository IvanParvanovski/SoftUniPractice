function holesCount(arr) {
    const holes = [
        1, 0, 0, 0, 1, 0, 1, 0, 2, 1
    ];

    function countHolesInNum(num) {
        return [...num.toString()].reduce((total, digit) => {
            if (isNaN(digit)) return total;
            return total + holes[Number(digit)];
        }, 0);
    }
       
    arr.sort((a, b) => {
        return countHolesInNum(a) - countHolesInNum(b);
    });

    return arr.join(', ');
}

console.log(holesCount([1000000000000000000000000000001, 15, 20]));