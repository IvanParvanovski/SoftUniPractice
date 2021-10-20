const {expect} = require('chai');
const {createCalculator} = require('./ex7-addSubtract');

describe('Ex7 AddSubtract Tests', () => {
    let instance = null;

    beforeEach(() => {
        instance = createCalculator();
    });

    describe('Test Returned Functions', () => {
        it('returns an object which contains add, subtract, get', () => {
            expect(instance).to.has.ownProperty('add');        
            expect(instance).to.has.ownProperty('subtract');        
            expect(instance).to.has.ownProperty('get');        
        });

        it('returns an object which contains functions', () => {
            const argumentsTypes = Object
                                    .keys(instance)
                                    .map((r) => typeof instance[r] == 'function');
                                    
            expect(argumentsTypes.every(x => x == true)).to.be.true;
        });

        describe('Test "add" function', () => {
            it('accepts an integer and adds it to the sum', () => {        
                const currentSum = instance.get();
                instance.add(5);
                const newValue = instance.get();
        
                expect(currentSum + 5).to.equal(newValue);
            });
    
            it('accepts a floating number and adds it to the sum', () => {        
                const currentSum = instance.get();
                instance.add(5.5);
                const newValue = instance.get();
        
                expect(currentSum + 5.5).to.equal(newValue);
            });

            it('accepts an integer as string and adds it to the sum', () => {        
                const currentSum = instance.get();
                instance.add('5');
                const newValue = instance.get();
        
                expect(currentSum + 5).to.equal(newValue);
            });

            it('accepts a floating number as string and adds it to the sum', () => {        
                const currentSum = instance.get();
                instance.add('5.5');
                const newValue = instance.get();
        
                expect(currentSum + 5.5).to.equal(newValue);
            });

            it('returns NaN when the argument is a text-string', () => {        
                instance.add('hi');
                const newSum = instance.get();
        
                expect(newSum).to.be.NaN;
            });
        });

        describe('Test "subtract" function', () => {
            it('accepts an integer and subtracts it of the sum', () => {        
                const currentSum = instance.get();
                instance.add(5);
                const newValue = instance.get();
        
                expect(currentSum + 5).to.equal(newValue);
            });
        
            it('accepts a floating number and subtracts it of the sum', () => {        
                const currentSum = instance.get();
                instance.subtract(5.5);
                const newValue = instance.get();
        
                expect(currentSum - 5.5).to.equal(newValue);
            })
        
            it('accepts an integer as string and subtracts it of the sum', () => {        
                const currentSum = instance.get();
                instance.subtract('5');
                const newValue = instance.get();
        
                expect(currentSum - 5).to.equal(newValue);
            });
            
            it('accepts a floating number as string and subtracts it of the sum', () => {        
                const currentSum = instance.get();
                instance.subtract('5.5');
                const newValue = instance.get();
        
                expect(currentSum - 5.5).to.equal(newValue);
            });
        
            it('returns NaN when the argument is a string', () => {        
                instance.subtract('hi');
                const newSum = instance.get();
        
                expect(newSum).to.be.NaN;
            });
        });

        describe('Test "get" function', () => {
            it('get function returns the value of the internal sum', () => {
                expect(instance.get()).to.equal(0);
            });
        });
    });

    it('has an internal sum that cannot be modified', () => {
        const currentValue = instance.value;
        expect(currentValue).to.equal(undefined);
    });
});
