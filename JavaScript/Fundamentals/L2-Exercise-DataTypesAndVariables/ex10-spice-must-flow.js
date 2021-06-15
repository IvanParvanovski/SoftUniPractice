function mine(startYield) {
    let total = 0;
    let days = 0;
    while (startYield >= 100) {
        total += startYield;
        total -= 26;
        
        if (total < 0) {
            total = 0;
        }

        startYield -= 10;
        days++;
    }

    total -= 26;
    if (total < 0) {
        total = 0;
    }
    
    console.log(days);
    console.log(total);
}

mine(111);