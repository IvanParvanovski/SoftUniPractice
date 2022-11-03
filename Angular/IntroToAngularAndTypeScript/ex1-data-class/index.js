var Data = /** @class */ (function () {
    function Data(method, uri, version, message, response, fulfilled) {
        if (fulfilled === void 0) { fulfilled = false; }
        this.method = method;
        this.uri = uri;
        this.version = version;
        this.message = message;
        this.response = response;
        this.fulfilled = fulfilled;
    }
    return Data;
}());
var myData = new Data('GET', 'http://google.com', 'HTTP/1.1', '');
console.log(myData);
