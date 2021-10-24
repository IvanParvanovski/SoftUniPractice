const {expect} = require('chai');
const mathEnforcer = require('../ex4-mathEnforcer');

describe('Ex4 MathEnforcer Test', () => {
    describe('addFive', () => {
        beforeEach(() => {
            testFunc = mathEnforcer.addFive;
        });

        it('when the parameter is a string return undefined', () => {
            expect(testFunc('random text')).to.be.undefined;
        });

        it('when the parameter is a string-number should return undefined', () => {
            expect(testFunc('1')).to.equal(undefined);
        });
    
        it('when the parameter is a positive number should return the number plus 5', () => {    
            expect(testFunc(1)).to.equal(6);
        });

        it('when the parameter is a negative number should return the number plus 5', () => {
            expect(testFunc(-1)).to.equal(4);
        });

        it('when the parameter is a double should return the number plus 5', () => {
            expect(testFunc(1.1).toFixed(2)).to.equal('6.10');
        });
    });

    describe('subtractTen', () => {
        beforeEach(() => {
            testFunc = mathEnforcer.subtractTen;
        });

        it('when the parameter is a string return undefined', () => {
            expect(testFunc('random text')).to.be.undefined
        });

        it('when the parameter is a string-number should return undefined', () => {
            expect(testFunc('10')).to.be.undefined;
        });
    
        it('when the parameter is a positive number should return the number subtracted by ten', () => {
            expect(testFunc(10)).to.equal(0);
        });

        it('when the parameter is a positive negative number should return the number subtracted by ten', () => {
            expect(testFunc(-1)).to.equal(-11);
        });

        it('when the parameter is a double should return the number subtracted by 10', () => {
            expect((testFunc(10.1)).toFixed(2)).to.equal('0.10');
        });
    });

    describe('sum', () => {
        beforeEach(() => {
            testFunc = mathEnforcer.sum;
        });

        it('when the first parameter is a string should return undefined', () => {
            expect(testFunc('random text', 0)).to.be.undefined;
        });
    
        it('when the second parameter is a string should return undefined', () => {
            expect(testFunc(0, 'random text')).to.be.undefined;
        });

        it('when the first parameter is a string-number should return undefined', () => {
            expect(testFunc('10', 0)).to.be.undefined;
        });

        it('when the second parameter is a string-number should return undefined', () => {
            expect(testFunc(0, '10')).to.be.undefined;
        });
    
        it('when the function both parameters are numbers should return their sum', () => {
            expect(testFunc(1, 1)).to.equal(2);
        });

        it('when the parameters are numbers with floating point should return their sum', () => {
            expect(testFunc(1.1, 2.2).toFixed(2)).to.equal('3.30');
        });
    });
});
