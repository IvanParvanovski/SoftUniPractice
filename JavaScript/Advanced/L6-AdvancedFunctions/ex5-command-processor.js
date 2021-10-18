function solution() {
    let message = '';

    function append(inputString) {
        message += inputString;
    }

    function removeStart(n) {
        message = message.slice(n);
    }

    function removeEnd(n) {
        message = message.slice(0, -n);
    }

    function print() {
        console.log(message);
    }

    return {
        append,
        removeStart,
        removeEnd,
        print,
    }
}

let firstZeroTest = solution();

firstZeroTest.append('hello');
firstZeroTest.append('again');
firstZeroTest.removeStart(3);
firstZeroTest.removeEnd(4);
firstZeroTest.print();


let secondZeroTest = solution();

secondZeroTest.append('123');
secondZeroTest.append('45');
secondZeroTest.removeStart(2);
secondZeroTest.removeEnd(1);
secondZeroTest.print();
