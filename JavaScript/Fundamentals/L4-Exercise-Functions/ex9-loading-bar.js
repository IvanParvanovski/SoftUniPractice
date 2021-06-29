function loadingBar(num) {
    let result = '';

    if (num < 100) {
        result += `${num}% [${'%'.repeat(num / 10)}${'.'.repeat(10 - num / 10)}]\n`;
        result += 'Still loading...';
    } else {
        result += '100% Complete!\n' + '[%%%%%%%%%%]';
    }

    return result;
}

console.log(loadingBar(30));