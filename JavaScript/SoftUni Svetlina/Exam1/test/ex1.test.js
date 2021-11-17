const { expect } = require("chai");
const { numLayers } = require('../ex1');

console.log(numLayers(1));

describe('Ex1 Tests', () => {
    it('should return a proper output when the input is a number', () => {
        const res = numLayers(1);

        expect(res).to.equal('0.001m');
    });

    it('should return a proper output when the input is string(number)', () => {
        const res = numLayers('1');

        expect(res).to.equal('0.001m');
    });

    it('should return NaN when the input is a string', () => {
        const res = numLayers('random text');

        expect(res).to.equal(NaN);
    });

    it('should return NaN when the input is an array', () => {
        const res = numLayers([]);

        expect(res).to.equal(NaN);
    });
});
