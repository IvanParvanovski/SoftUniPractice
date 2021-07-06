function smallestNumbers(numbers) {
    console.log(numbers
        .sort((a, b) => a - b)
        .slice(0, 2)
        .join(' ')
    );
}

smallestNumbers([1, -1, -3, -2, 4, 5]);