function secondLargest(numbers) {
    console.log(numbers.sort((a, b) => Number(b) - Number(a))[1]);
}


secondLargest([10, 40, 30, 20, 50]);
secondLargest([25, 143, 89, 13, 105]);
secondLargest([54, 23, 11, 17, 10]);
