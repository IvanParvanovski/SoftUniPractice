function palindromeIntegers(numbers) {
    function isPalindrome(num) {
        for (let i = 0; i < num.length / 2; i++) {
            if (num[i] != num[num.length - i - 1]) {
                return false;
            }
        }

        return true;
    }

    for (let num of numbers) {
        let numAsString = num.toString();
        console.log(isPalindrome(numAsString));
    }
}

palindromeIntegers([123, 323, 421, 121]);