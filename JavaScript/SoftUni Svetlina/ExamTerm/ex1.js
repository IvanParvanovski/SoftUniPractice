function solve(n) { 
    let sugar = 0;

    for (let i = 1; i < n + 1; i++) {
        sugar += (50 * 0.05) + (50 * 0.18);

        if (i % 5 == 0) {
            sugar += 75 * 0.20;
        }
    }

    return `You have consumed ${sugar} grams of sugar`;
}

solve(9);
