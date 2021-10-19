const { assert, expect } = require("chai");
const isSymmetric = require('./ex5-checkForSymmetry');


describe('Ex5 CheckForSymmetry', () => {
    it('returns true for symmetric array', () => {
        expect(isSymmetric([1, 2, 2, 1])).to.be.true;
    });

    it('returns false for non-symmetric array', () => {
        expect(isSymmetric([1, 2, 3])).to.be.false;
    });

    it('returns false for non-array', () => {
        expect(isSymmetric('5')).to.be.false;
    });

    it('returns false for different values', () => {
        expect(isSymmetric([1, '2', 2, 1])).to.be.false;
    });

    it('returns true for odd values', () => {
        expect(isSymmetric([1, 2, 1])).to.be.true;
    })

    it('returns false for empty array', () => {
        expect(isSymmetric([])).to.be.true;
    })
});
