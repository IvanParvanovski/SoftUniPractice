var KeyValuePair = /** @class */ (function () {
    function KeyValuePair() {
        this.keys = [];
        this.values = [];
    }
    KeyValuePair.prototype.setKeyValue = function (key, value) {
        this.keys.push(key);
        this.values.push(value);
    };
    KeyValuePair.prototype.display = function () {
        for (var i = 0; i < this.keys.length; i++) {
            console.log("key = ".concat(this.keys[i], ", value = ").concat(this.values[i]));
        }
    };
    return KeyValuePair;
}());
var kvp = new KeyValuePair();
kvp.setKeyValue(1, 'Steve');
kvp.display();
