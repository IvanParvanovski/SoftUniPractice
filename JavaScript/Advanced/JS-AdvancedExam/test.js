const {expect} = require('chai');
const library = require('./library');
console.log(library);

describe('Tests', () => {
    describe('calcPriceOfBook', () => {
        beforeEach(() => {
            func = library.calcPriceOfBook;
        });

        it('when the nameOfBook is an integer should return Invalid input', () => {
            expect(() => func(1, 1)).to.be.throw('Invalid input');
        });

        it('when the nameOfBook is an array should return Invalid input', () => {
            expect(() => func([], 1)).to.be.throw('Invalid input');
        });

        it('when the year is a string should return Invalid input', () => {
            expect(() => func('message', 'random text')).to.be.throw('Invalid input');
        });

        it('when the year is a double should return Invalid input', () => {
            expect(() => func('message', 1.1)).to.be.throw('Invalid input');
        });

        it('when the year is under or equal to 1980 should have a discount', () => {
            const result = func('myBook', 1980);

            expect(result).to.be.equal('Price of myBook is 10.00');
        });

        it('when the year is above 1980 should not have a discount', () => {
            const result = func('myBook', 1981);

            expect(result).to.be.equal('Price of myBook is 20.00');
        });
    });

    describe('findBook', () => {
        beforeEach(() => {
            func = library.findBook;
        });

        it('when the bookArray is zero should throw Error', () => {
            expect(() => func([], 'random message')).to.throw('No books currently available');
        });

        it('when the searchedBook is NOT in the array should return a message', () => {
            const result = func(['Troy', 'Torronto'], 'Sparta');

            expect(result).to.equal('The book you are looking for is not here!');
        });

        it('when the searchedBook is NOT in the array should return a message', () => {
            const result = func(['Financer', 'Titan', 'Stoik'], 'Meri Popins');

            expect(result).to.equal('The book you are looking for is not here!');
        });

        it('when the searchedBook is in the array should return a message', () => {
            const result = func(['Troy', 'Torronto'], 'Troy');

            expect(result).to.equal('We found the book you want.');
        });

        it('when the searchedBook is in the array should return a message', () => {
            const result = func(['Financier', 'Titan', 'Stoik'], 'Financier');

            expect(result).to.equal('We found the book you want.');
        });
    });

    describe('arrangeTheBooks', () => {
        beforeEach(() => {
            func = library.arrangeTheBooks;
        });

        it('when the countBooks is a negative number should raise an exception', () => {
            expect(() => func(-1)).to.throw('Invalid input');
        });

        it('when the countBooks is a double should raise an exception', () => {
            expect(() => func(0.1)).to.throw('Invalid input');
        });

        it('when the countBooks is a string should raise an exception', () => {
            expect(() => func('random message')).to.throw('Invalid input');
        });
    
        it('when there is no more space on the shelves should return a message', () => {
            const result = func(41);

            expect(result).to.equal('Insufficient space, more shelves need to be purchased.');
        });

        it('when there is space on the shelves should return a message', () => {
            const result = func(40);

            expect(result).to.equal('Great job, the books are arranged.');
        });
    });
});