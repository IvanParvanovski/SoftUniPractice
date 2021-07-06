function factorialDivision(fisrtNum, secondNum) {
    function factorial(num) {
        let result = 1;

        for (let i = num; i > 0; i--) {
            result *= i;
        }

        return result;
    }

    console.log((factorial(fisrtNum) / factorial(secondNum)).toFixed(2));
}

factorialDivision(5, 2);