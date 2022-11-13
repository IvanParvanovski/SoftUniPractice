function softUniBarIncome(input) {
    const regexPattern = /%(?<customer>[A-Z][a-z]+)%.*?<(?<product>\w+)>.*?\|(?<count>\d+)\|.*?(?<price>\d+(?:\.\d+)?)\$/;
    let total = 0;

    for (const customerData of input) {
        if (customerData == 'end of shift') {
            break;
        } 

        const result = regexPattern.exec(customerData);
        
        if (result) {
            const consumption =  Number(result.groups['count']) * Number(result.groups['price']);
            total += consumption;

            console.log(`${result.groups['customer']}: ${result.groups['product']} - ${consumption.toFixed(2)}`);
        }
    }

    console.log(`Total income: ${total.toFixed(2)}`);
}

// softUniBarIncome([
//     '%InvalidName%<Croissant>|2|10.3$', 
//     '%Peter%<Gum>1.3$', 
//     '%Maria%<Cola>|1|2.4', 
//     '%Valid%<Valid>valid|10|valid20$', 
//     'end of shift'])

softUniBarIncome([
    "%George%<Croissant>|2|10.3$",
    "%Peter%<Gum>|1|1.3$",
    "%Maria%<Cola>|1|2.4$",
    "end of shift"
]);
