function checkIfIsLeap(year) {
    if (year % 4 === 0) {
        if (year % 100 !== 0) {
            console.log('yes');
        } else if (year % 400 === 0) {
            console.log('yes');
        } else {
            console.log('no');
        }
    } else {
        console.log('no');
    }
}

checkIfIsLeap(1984);
checkIfIsLeap(2003);
checkIfIsLeap(4);
