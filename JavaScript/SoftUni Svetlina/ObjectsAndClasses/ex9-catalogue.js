function catalogue(input) {
    const result = []
    
    for (const product of input) {
        const [name, price] = product.split(' : ');
        result.push({ name, price });
    }

    let lastLetter = '';
    for (const r of result.sort((a, b) => a.name.localeCompare(b.name))) {
        const currentLetter = r.name[0];

        if (currentLetter.toUpperCase() != lastLetter.toUpperCase()) {
            console.log(currentLetter);
            lastLetter = currentLetter;
        }

        console.log(`  ${r.name}: ${r.price}`);
    }
}

catalogue([
    'app : 15',
    'Appricot : 20.4', 
    'Fridge : 1500', 
    'TV : 1499', 
    'Deodorant : 10', 
    'Boiler : 300', 
    'Apple : 1.25', 
    'Anti-Bug Spray : 15', 
    'T-Shirt : 10'])
    