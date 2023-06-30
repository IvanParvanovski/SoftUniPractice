class Hex {
    constructor(value) {
        this.value = value;
    }

    valueOf() {
        return this.value;
    }

    toString() {
        return `0x${this.value.toString(16).toUpperCase()}`;
    }

    plus(number) {
        if (number instanceof Hex) {
            number = number.valueOf();
        }
        return new Hex(this.value + number);
    }

    minus(number) {
        if (number instanceof Hex) {
            number = number.valueOf();
        }
        return new Hex(this.value - number);
    }

    static parse(string) {
        return parseInt(string, 16);
    }
}