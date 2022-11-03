class Box<T> {
    public elements: T[];

    constructor() {
        this.elements = [];
    }

    add(element: T) {
        this.elements.push(element);
    }

    remove() {
        this.elements.pop();
    }

    get count(): number {
        return
    }
}