function doubleString(message, count) {
    const arr = [];

    for (const symbol of message) {
        for (let i = 0; i < count; i++) {
            arr.push(symbol);
        }
    }

    console.log(arr.join(''));
}

doubleString('abc', 5);