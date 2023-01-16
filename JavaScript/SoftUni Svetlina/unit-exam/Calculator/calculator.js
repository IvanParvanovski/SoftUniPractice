let calculator = {
    add: function(arr1, arr2) {
        return [arr1[0] + arr2[0], arr1[1] + arr2[1]];
    },
    length: function(arr) {
        return Math.sqrt(Math.pow(arr[0], 2) + Math.pow(arr[1], 2));
    }
};

// console.log(calculator.add([1, 1], [1, 0]));
// console.log(calculator.length([3, -4]));

module.exports = calculator;
