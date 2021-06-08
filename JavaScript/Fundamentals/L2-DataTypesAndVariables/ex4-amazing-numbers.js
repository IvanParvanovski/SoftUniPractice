function isAmazing(number) {
    let total = 0;
    foreach (digit in number) {
        total += Numeric(digit);
    }
    console.log(total);
}

isAmazing(1233);