function checkEqualSum(numbers) {
    let hasIndex = false;
    let i = 0;

    for (; i < numbers.length; i++) {
        let leftSum = 0;
        let rightSum = 0;

        for (let j = 0; j < i; j++) {
            let currentNum = numbers[j];
            leftSum += currentNum;
        }

        for (let k = i + 1; k < numbers.length; k++) {
            let currentNum = numbers[k];
            rightSum += currentNum
        }

        if (leftSum == rightSum) {
            hasIndex = true;
            break;
        }
    }

    console.log(hasIndex ? i : 'no');
}

checkEqualSum([1, 2, 3, 3]);
checkEqualSum([1, 2])