function fancyBarcodes(input) {
    input.shift();

    let regexPattern = /(?:@#+)([A-Z](?:[A-Za-z]|\d){4,}[A-Z])(?:@#+)/;
    let regex = new RegExp(regexPattern);
    
    let digits = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '0',
    ];

    for (let barcode of input) {
        let matchTokens = barcode.match(regex);

        if (matchTokens != null) {
            let match = matchTokens[0];
            let productGroup = '';

            for (let symbol of match) {
                if (digits.includes(symbol)) {
                    productGroup += symbol;
                }
            }
            
            console.log(`Product group: ${productGroup.length > 0 ? productGroup : '00'}`);
        } else {
            console.log('Invalid barcode');
        }
    }
}

fancyBarcodes(["6",
"@###Val1d1teM@###",
"@#ValidIteM@#",
"##InvaliDiteM##",
"@InvalidIteM@",
"@#Invalid_IteM@#",
"@#ValiditeM@#"]);

// fancyBarcodes(["3",
// "@#FreshFisH@#",
// "@###Brea0D@###",
// "@##Che4s6E@##"]);
