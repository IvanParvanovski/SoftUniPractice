const { assert } = require("chai");
const {sum} = require('./ex4-sumOfNumbers');

describe('Ex4 SumOfNumbers Tests', () => {
    it('Sum numbers with string', () => {
        assert(sum([1, '2', 3, 4]), 10);
    });

    
})
