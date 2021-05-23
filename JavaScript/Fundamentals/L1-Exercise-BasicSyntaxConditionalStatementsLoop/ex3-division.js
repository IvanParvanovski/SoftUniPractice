function devide(num) {
    let devider = 0;

    if (num % 2 === 0) {
        devider = 2;
    }

    if (num % 3 === 0) {
        devider = 3;
    }

    if (num % 6 === 0) {
        devider = 6;
    } 

    if (num % 7 === 0) {
        devider = 7;
    }

    if (num % 10 === 0) {
        devider = 10;
    }

    if (devider === 0) {
        console.log('Not divisible');
    } else {
        console.log(`The number is divisible by ${devider}`);
    }

}

devide(30);
devide(15);
devide(12);
devide(1643);
