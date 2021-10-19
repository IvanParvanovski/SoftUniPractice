function createCalculator() {
    let value = 0;
    return {
        add: function(num) { value += Number(num); },
        subtract: function(num) { value -= Number(num); },
        get: function() { return value; }
    }
}

const calculator = createCalculator();
        
// const addFunction = calculator.add;
// const currentTotalSum = calculator.value;        
// addFunction(5);
// const changedTotalSum = calculator.value;

console.log(calculator);
// expect(currentTotalSum + 5).to.equal(changedTotalSum);

module.exports = {
    createCalculator,
};