function sameNumber(number) {
    let numberAsString = number.toString();

    let areTheSame = true;
    let total = 0;
    let startDigit = numberAsString[0];

    for (let digit of numberAsString) {
        total += Number(digit);

        if (digit != startDigit) {
            areTheSame = false;
        }
    }

    console.log(areTheSame);
    console.log(total);
}

sameNumber(2222222);
sameNumber(1234);
