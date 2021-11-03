function averageLength(...input) {
    let totalSum = 0;

    for (const string of input) {
        totalSum += string.length;
    }

    console.log(totalSum);
    console.log(Math.floor(totalSum / input.length));
}

averageLength('chocolate', 'ice cream', 'cake');

