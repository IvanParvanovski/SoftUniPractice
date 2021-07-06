function oddNumbers(numbers) {
    // let result = numbers
    //     .filter((x, i) => i % 2 != 0)
    //     .map(x => x * 2)
    //     .reverse()
    //     .join(' ');
    
    let filtered = numbers.filter((x, i) => i % 2 != 0);
    let mapped = filtered.map(x => x * 2);
    console.log(mapped.reverse().join(' '));
    // console.log(result);
}

oddNumbers([10, 15, 20, 25])