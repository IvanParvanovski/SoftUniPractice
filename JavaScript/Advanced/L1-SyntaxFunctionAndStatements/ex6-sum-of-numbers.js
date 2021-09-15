function numbersSum(num1, num2) {
    num1 = Number(num1);
    num2 = Number(num2);

    // let start;
    // let end;

    // if (num1 < num2) {
    //     start = num1;
    //     end = num2;
    // } else {
    //     start = num2;
    //     end = num1;
    // }

    let total = 0;
    for (let i = num1; i <= num2; i++) {
        total += i;
    }

    console.log(total);
}

numbersSum('-8', '20');
