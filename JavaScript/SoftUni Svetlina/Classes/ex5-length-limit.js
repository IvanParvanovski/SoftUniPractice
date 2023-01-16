class Stringer {
    constructor(innerString, innerLength) {
        this.innerString = innerString;
        this.innerLength = innerLength;

        this.initializedString = innerString;
    }

    increase(length) {
        this.innerLength += length;
    }

    decrease(length) {
        this.innerLength -= length;

        if (this.innerLength < 0) {
            this.innerLength = 0;
        }
    }

    toString() {
        if (this.innerString.length > this.innerLength) {
            const symbolsToRemove = this.innerString.length - this.innerLength;
            const temp = this.innerString.substring(0, symbolsToRemove) + '...';

            return temp;
        } else if (this.innerLength == 0) {
            return '...';
        }

        return this.innerString;
    }
}

console.log('Test'.substring(0, ))

let test = new Stringer("Test", 5);
console.log(test.toString()); // Test

test.decrease(3);
console.log(test.toString()); // Te...

test.decrease(5);
console.log(test.toString()); // ...
