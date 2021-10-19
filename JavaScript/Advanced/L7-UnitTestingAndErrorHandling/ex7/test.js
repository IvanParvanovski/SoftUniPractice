const {expect} = require('chai');
const {createCalculator} = require('./ex7-addSubtract');

describe('Ex7 AddSubtract Tests', () => {
    it('returns an object which contains add, subtract, get', () => {
        const result = createCalculator();
        
        expect(Object.keys(result).includes('add')).to.be.true;
        expect(Object.keys(result).includes('subtract')).to.be.true;
        expect(Object.keys(result).includes('get')).to.be.true;
    });

    it('returns an object which contains functions', () => {
        const result = createCalculator();
        const argumentsTypes = Object
                                .keys(result)
                                .map((r) => typeof result[r] == 'function');
                                
        expect(argumentsTypes.every(x => x == true)).to.be.true;
    });

    it('has an internal sum that cannot be modified', () => {
        const currentValue = createCalculator().value;
        expect(currentValue).to.equal(undefined);
    });

    it('add function accepts an integer and adds to the sum', () => {
        const calculator = createCalculator();
        
        const currentSum = calculator.get();
        calculator.add(5);
        const newValue = calculator.get();

        expect(currentSum + 5).to.equal(newValue);
    });

    it('add function accepts a floating number and adds it', () => {
        const calculator = createCalculator();
        
        const currentSum = calculator.get();
        calculator.add(5.5);
        const newValue = calculator.get();

        expect(currentSum + 5.5).to.equal(newValue);
    })

    it('add function accepts an integer as string and adds to the sum', () => {
        const calculator = createCalculator();
        
        const currentSum = calculator.get();
        calculator.add('5');
        const newValue = calculator.get();

        expect(currentSum + 5).to.equal(newValue);
    });
    
    it('add function accepts a floating number as string and adds to the sum', () => {
        const calculator = createCalculator();
        
        const currentSum = calculator.get();
        calculator.add('5.5');
        const newValue = calculator.get();

        expect(currentSum + 5.5).to.equal(newValue);
    });

    it('add function returns NaN when the argument is a string', () => {
        const calculator = createCalculator();
        
        calculator.add('hi');
        const newSum = calculator.get();

        expect(newSum).to.be.NaN;
    });

    it('subtract function accepts an integer and subtracts it of the sum', () => {
        const calculator = createCalculator();
        
        const currentSum = calculator.get();
        calculator.add(5);
        const newValue = calculator.get();

        expect(currentSum + 5).to.equal(newValue);
    });

    it('subtract function accepts a floating number and subtracts it of the sum', () => {
        const calculator = createCalculator();
        
        const currentSum = calculator.get();
        calculator.subtract(5.5);
        const newValue = calculator.get();

        expect(currentSum - 5.5).to.equal(newValue);
    })

    it('subtract function accepts an integer as string and subtracts it of the sum', () => {
        const calculator = createCalculator();
        
        const currentSum = calculator.get();
        calculator.subtract('5');
        const newValue = calculator.get();

        expect(currentSum - 5).to.equal(newValue);
    });
    
    it('subtract function accepts a floating number as string and subtracts it of the sum', () => {
        const calculator = createCalculator();
        
        const currentSum = calculator.get();
        calculator.subtract('5.5');
        const newValue = calculator.get();

        expect(currentSum - 5.5).to.equal(newValue);
    });

    it('subtract function returns NaN when the argument is a string', () => {
        const calculator = createCalculator();
        
        calculator.subtract('hi');
        const newSum = calculator.get();

        expect(newSum).to.be.NaN;
    });

    it('get function returns the value of the internal sum', () => {
        const calculator = createCalculator();

        expect(calculator.get()).to.equal(0);
    });
});
