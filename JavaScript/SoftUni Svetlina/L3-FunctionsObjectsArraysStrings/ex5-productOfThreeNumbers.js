function productOfThreeNumbers(numbers) {
    const [a, b, c] = numbers;
    const result = a * b * c;

    console.log(result >= 0 ? "Positive" : "Negative");
}