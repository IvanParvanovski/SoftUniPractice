const { expect } = require("chai");
const {sum} = require('./ex4-sumOfNumbers');

describe('Ex4 SumOfNumbers Tests', () => {
    it('sum numbers with string', () => {
        expect(sum([1, '2', 3, 4])).to.equal(10);
    });

    it('throws exception when num is invalid type', () => {
        expect(sum('hi')).to.be.NaN;
    });

    it('sum negative numbers', () => {
        expect(sum([-1, -2, 3])).to.equal(0);
    });
})
