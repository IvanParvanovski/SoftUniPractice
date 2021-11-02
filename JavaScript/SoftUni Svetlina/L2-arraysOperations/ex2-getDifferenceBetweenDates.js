/**
 * 
 * @param {Date} firstDate 
 * @param {Date} secondDate 
 */
function getDifference(firstDate, secondDate) {
    return Math.abs(
        (firstDate.getTime() - secondDate.getTime()) / 
        86400000
    );
}

console.log(getDifference(
    new Date(2021, 11, 2),
    new Date(2021, 10, 27),
));
