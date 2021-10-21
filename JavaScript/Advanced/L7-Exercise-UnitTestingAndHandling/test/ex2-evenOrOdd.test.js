const {expect} = require('chai');
const {isOddOrEven} = require('../ex2-evenOrOdd');

describe('Ex2 IsOddOrEven Tests', () => {
    it('return undefined if the input is double', () => {
        const result = isOddOrEven(1.1);

        expect(result).to.be.undefined;
    });

    it('return undefined if the input is int', () => {
        const result = isOddOrEven(1);

        expect(result).to.be.undefined;
    });

    it('return undefined if the input is array', () => {
        const result = isOddOrEven([]);

        expect(result).to.be.undefined;
    });

    it('return even when the string has even length', () => {
        const result = isOddOrEven('name');

        expect(result).to.equals('even');
    });

    it('return even when the string has even length', () => {
        const result = isOddOrEven('test message');

        expect(result).to.equals('even');
    });

    it('return even when the string is empty', () => {
        const result = isOddOrEven('');

        expect(result).to.equals('even');
    })

    it('retun odd when the string has odd length', () => {
        const result = isOddOrEven('hello');
        expect(result).to.equals('odd');
    });

    it('retun odd when the string has odd length', () => {
        const result = isOddOrEven('message');

        expect(result).to.equals('odd');
    });

});
