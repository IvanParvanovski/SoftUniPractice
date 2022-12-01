function cutAndReverse(input) {
    const leftPart = [];
    const rightPart = []
    const middle = Math.round(input.length / 2);

    for (let i = 0; i < middle; i++) {
        leftPart.push(input[i]);
    }

    for (let i = middle; i < input.length; i++) {
        rightPart.push(input[i]);
    }

    console.log(leftPart.reverse().join(''));
    console.log(rightPart.reverse().join(''));
}

cutAndReverse('abcde');
cutAndReverse('sihToDtnaCuoYteBIboJsihTtAdooGoSmI');
