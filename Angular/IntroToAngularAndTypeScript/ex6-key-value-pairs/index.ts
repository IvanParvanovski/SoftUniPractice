class KeyValuePair<K, V> {
    public keys: K[];
    public values: V[];

    constructor() {
        this.keys = [];
        this.values = [];
    }

    setKeyValue(key: K, value: V) {
        this.keys.push(key);
        this.values.push(value);
    }

    display() {
        for (let i = 0; i < this.keys.length; i++) {
            console.log(`key = ${this.keys[i]}, value = ${this.values[i]}`);
        }
    }
}

let kvp = new KeyValuePair<number, string>();
kvp.setKeyValue(1, 'Steve');
kvp.display();
