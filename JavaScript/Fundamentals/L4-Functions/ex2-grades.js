function schoolYearResult(grade) {
    let result;
    if (grade < 3) {
        result = 'Fail';
    } else if (grade < 3.50) {
        result = 'Poor';
    } else if (grade < 4.50) {
        result = 'Good';
    } else if (grade < 5.50) {
        result = 'Very good';    
    } else {
        result = 'Excellent';
    }

    return `${result} (${grade != 2 ? grade.toFixed(2) : grade})`;
}

console.log(schoolYearResult(1)); // Fail (2)
console.log(schoolYearResult(1.50)); // Fail (2)
console.log(schoolYearResult(-1)); // Fail (2)

console.log(schoolYearResult(2)); // Fail (2)
console.log(schoolYearResult(2.15)); // Fail (2)
console.log(schoolYearResult(2.00)); // Fail (2)
console.log(schoolYearResult(-2)); // Fail (2)

console.log(schoolYearResult(3)); // Poor (3)
console.log(schoolYearResult(3.33)); // Poor (3.33)
console.log(schoolYearResult(3.30)); // Poor (3.30)
console.log(schoolYearResult(-3)); // Fail (2)

console.log(schoolYearResult(4)); // Good (4)
console.log(schoolYearResult(4.44)); // Good (4.44)
console.log(schoolYearResult(4.40)); // Good (4.40)
console.log(schoolYearResult(-4)); // Fail (2)

console.log(schoolYearResult(5)); // Very good (5)
console.log(schoolYearResult(5.20)); // Very good (5.20)
console.log(schoolYearResult(-5)); // Fail (2)

console.log(schoolYearResult(6)); // Excellent (6)
console.log(schoolYearResult(6.60)); // Excellent (6) 
console.log(schoolYearResult(-6)); // Fail (2)
console.log(schoolYearResult(5.50)); // Excellent (5.50)
console.log(schoolYearResult(5.55)); // Excellent (5.55)
