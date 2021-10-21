const {expect} = require('chai');
const {lookupChar} = require('../ex3-charLookup');

describe('Ex3 CharLookup Tests', () => {
    it('return undefined if the first parameter is undefined', () => {
        const result = lookupChar(undefined, 0)

        expect(result).to.be.undefined;
    });

    it('return undefined if the first parameter is int', () => {
        const result = lookupChar(1.1, 0);

        expect(result).to.be.undefined;
    });

    it('return undefined if the second parameter is undefined', () => {
        const result = lookupChar('test', undefined);

        expect(result).to.be.undefined;
    });

    it('return undefined if the second parameter is double', () => {
        const result = lookupChar('test', 2.222);
        
        expect(result).to.be.undefined; 
    });

    it('return "Incorrect index" if the index is negative', () => {
        const result = lookupChar('test', -1);
        
        expect(result).to.be.equal('Incorrect index');
    });

    it('return "Incorrect index" if the index is equal to the string length', () => {
        const result = lookupChar('test', 4);

        expect(result).to.be.equal('Incorrect index');
    });

    it('return "Incorrect index" if the index is above the string length', () => {
        const result = lookupChar('test', 5);

        expect(result).to.be.equal('Incorrect index');
    });

    it('return "Incorrect index" if the string is empty', () => {
        const result = lookupChar('', 0);
        
        expect(result).to.be.equal('Incorrect index');
    });

    it('return the correct character of the string when the both parameters are valid', () => {
        const result = lookupChar('message', 1);

        expect(result).to.be.equal('e');
    });

    it('return the correct character of the string when the both parameters are valid', () => {
        const result = lookupChar('random', 4);

        expect(result).to.be.equal('o');
    });
});
