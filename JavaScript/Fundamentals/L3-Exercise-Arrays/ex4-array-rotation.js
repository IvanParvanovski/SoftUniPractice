function arrayRotation(numbers, rotations) {
    for (let i = 0; i < rotations; i++) {
        let num = numbers.shift();
        numbers.push(num);
    }
    console.log(numbers.join(' '));
}

arrayRotation([51, 47, 32, 61, 21], 2);
