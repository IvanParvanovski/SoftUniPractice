function combs(num) {
    for (let i = 0; i < num; i++) {
        for (let j = 0; j < num; j++) {
            for (let k = 0; k < num; k++) {
                console.log(`${String.fromCharCode(i + 97)}` +
                            `${String.fromCharCode(j + 97)}` +
                            `${String.fromCharCode(k + 97)}`);
            }
        }
    }
}
combs(3);
