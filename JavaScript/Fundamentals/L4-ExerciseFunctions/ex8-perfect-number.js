function perfectNum(num) {
    function getAllPositiveDivisors(num) {
        let divisors = []
        
        for (let i = 1; i < num; i++) {
            if (num % i == 0) {
                divisors.push(i);
            }
        } 

        return divisors;
    }

    function sumOfNumbers(numbers) {
        let result = 0;

        for (let num of numbers) {
            result += num;
        }

        return result;
    }

    let result = '';

    if (sumOfNumbers(getAllPositiveDivisors(num)) == num) {
        result = 'We have a perfect number!';
    } else {
        result = 'It\'s not so perfect.';
    }

    console.log(result);
}
perfectNum(6);
perfectNum(28);
perfectNum(1236498);
