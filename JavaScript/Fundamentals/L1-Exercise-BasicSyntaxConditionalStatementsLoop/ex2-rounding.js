function rounding(number, precision) {
    if (precision > 15) {
        precision = 15;
    }
    console.log(parseFloat(number.toFixed(precision)));
}

rounding(10.5, 3)
rounding(3.1415926535897932384626433832795,2);