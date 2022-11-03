class Data {
    constructor(
        public method: string,
        public uri: string,
        public version: string,
        public message: string,
        public response?: string,
        public fulfilled: boolean = false
    ) {}
}

let myData = new Data('GET', 'http://google.com', 'HTTP/1.1', '')
console.log(myData);
