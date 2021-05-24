function calculateBitcoin(gold) {
    let day = 1;
    let bitcoin = 0;
    let firstBitcoinDay = 0;
    let money = 0;

    while (true) {
        if (gold.length == 0) {
            break;
        }

        let goldBar = gold.shift();
        if (day % 3 == 0) {
            goldBar -= 0.3 * goldBar; 
        } 

        money += goldBar * 67.51;
        while (money >= 11949.16) {
            if (bitcoin == 0) {
                firstBitcoinDay = day;
            }
            money -= 11949.16; 
            bitcoin++;
        }

        day++;
    }
    console.log(`Bought bitcoins: ${bitcoin}`);
    if (firstBitcoinDay != 0) {
        console.log(`Day of the first purchased bitcoin: ${firstBitcoinDay}`);                
    }
    console.log(`Left money: ${money.toFixed(2)} lv.`);
}

// calculateBitcoin([100, 200, 300]);
calculateBitcoin([50, 100]);
// calculateBitcoin([3124.15, 504.212, 2511.124]);
