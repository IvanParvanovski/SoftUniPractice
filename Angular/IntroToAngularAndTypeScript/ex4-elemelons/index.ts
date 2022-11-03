class Melon {
    public weight: number;
    public melonSort: string;

    constructor(weight: number, melonSort: string) {
        this.weight = weight;
        this.melonSort = melonSort;
    }
}

class Watermelon extends Melon {
    private elementIndex: number;

    constructor(weight: number, melonSort: string) {
        super(weight, melonSort);
        this.elementIndex = weight * melonSort.length;
    }

    getElementIndex(): number {
        return this.elementIndex;
    }

    toString(): string {
        return [
            'Element Water',
            `Sort: ${this.melonSort}`,
            `Element Index: ${this.getElementIndex()}`
        ].join('\n');
    }
}

class Firemelon extends Melon {
    private elementIndex: number;

    constructor(weight: number, melonSort: string) {
        super(weight, melonSort);
        this.elementIndex = weight * melonSort.length;
    }

    getElementIndex(): number {
        return this.elementIndex;
    }

    toString(): string {
        return [
            'Element Fire',
            `Sort: ${this.melonSort}`,
            `Element Index: ${this.getElementIndex()}`
        ].join('\n');
    }
}

class Earthmelon extends Melon {
    private elementIndex: number;

    constructor(weight: number, melonSort: string) {
        super(weight, melonSort);
        this.elementIndex = weight * melonSort.length;
    }

    getElementIndex(): number {
        return this.elementIndex;
    }

    toString(): string {
        return [
            'Element Earth',
            `Sort: ${this.melonSort}`,
            `Element Index: ${this.getElementIndex()}`
        ].join('\n');
    }
}

class Airmelon extends Melon {
    private elementIndex: number;

    constructor(weight: number, melonSort: string) {
        super(weight, melonSort);
        this.elementIndex = weight * melonSort.length;
    }

    getElementIndex(): number {
        return this.elementIndex;
    }

    toString(): string {
        return [
            'Element Air',
            `Sort: ${this.melonSort}`,
            `Element Index: ${this.getElementIndex()}`
        ].join('\n');
    }
}




let watermelon : Watermelon = new Watermelon(12.5, "Kingsize");
console.log(watermelon.toString());
