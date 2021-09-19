function evenPositionElement(numbers) {
    console.log(numbers.filter((x, i) => {
        if (i % 2 == 0) {
            return x;
        }
    }).join(' '));
}

function authorSolution(numbers) {
    let result = [];

    for (let i = 0; i < numbers.length; i += 2) {
        result[result.length] = numbers[i];
    }

    console.log(result.join(' '));
}

evenPositionElement(['20', '30', '40','50', '60'])