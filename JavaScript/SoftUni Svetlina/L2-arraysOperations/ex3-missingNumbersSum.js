function getSum(arr) {
    let total = 0;
    arr.sort((a, b) => a - b);
    
    for (let i = 0; i < arr.length - 1; i++) {
        const currentNum = arr[i];
        const nextNum = arr[i + 1];

        for (let j = currentNum + 1; j < nextNum; j++) {
            total += j;
        }
    }

    console.log(total);
}

getSum([1, 5, 10]);
