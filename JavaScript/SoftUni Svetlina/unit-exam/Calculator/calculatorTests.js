const { expect } = require('chai');
const createCalculator = require('./calculator.js');

describe('Calculator Tests', function() {
    it('add positive numbers', () => {
        expect(createCalculator.add([1, 2], [3, 4])).to.eql([4, 6]);
    });

    it('add negative numbers', () => {
        expect(createCalculator.add([-1, -1], [-1, 0])).to.eql([-2, -1]);
    });

    it('add zeros', () => {
        expect(createCalculator.add([0, 0], [0, 0])).to.eql([0, 0]);
    });

    it('add strings', () => {
        expect(createCalculator.add(['random', ''], ['random', ''])).to.eql(['randomrandom', '']);
    });

    it('sqrt of aggregate of two numbers', () => {
        expect(createCalculator.length([3, -4])).to.equals(5);
    });

    it('sqrt of zeros', () => {
        expect(createCalculator.length([0, 0])).to.equals(0);
    })
})
