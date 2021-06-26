function repeatedStrings(text, count) {
    let result = '';

        for (let i = 0; i < count; i++) {
            result += text;
        }

    return result;
}

console.log(repeatedStrings('hi', 3));

