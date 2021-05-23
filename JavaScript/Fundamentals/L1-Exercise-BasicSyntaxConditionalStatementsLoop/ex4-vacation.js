function calculateCost(peopleCount, groupType, day) {
    let dayCost;
    let discount = 0;

    switch (groupType) {
        case 'Students':
            if (day == 'Friday') {
                dayCost = 8.45;        
            } else if (day == 'Saturday') {
                dayCost = 9.80;
            } else if (day == 'Sunday') {
                dayCost = 10.46;
            }

            if (peopleCount >= 30) {
                discount = 0.15;
            }

            break;
        
        case 'Business':
            if (day == 'Friday') {
                dayCost = 10.90;        
            } else if (day == 'Saturday') {
                dayCost = 15.60;
            } else if (day == 'Sunday') {
                dayCost = 16;
            }

            if (peopleCount >= 100) {
                peopleCount -= 10
            }

            break;
        
        case 'Regular':
            if (day == 'Friday') {
                dayCost = 15;        
            } else if (day == 'Saturday') {
                dayCost = 20;
            } else if (day == 'Sunday') {
                dayCost = 22.50;
            }

            if (peopleCount >= 10 && peopleCount <= 20) {
                discount = 0.05;
            }

            break;    
    }

    let total = peopleCount * dayCost;
    total -= discount * total
    console.log(`Total price: ${total.toFixed(2)}`);
}

calculateCost(30, 'Students', 'Sunday');
calculateCost(40, 'Regular', 'Saturday');
