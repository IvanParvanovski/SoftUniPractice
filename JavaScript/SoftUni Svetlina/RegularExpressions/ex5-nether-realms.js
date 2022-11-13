function netherRealm(input) {
    const participants = input.split(/[, ]+/g);

    const healthPattern = /[^\d\+\-\*\/\.]/g;
    const damagePattern = /(\+?\d+(?:\.\d+)?)|(\-?\d+(?:\.\d+)?)/g;
    const arithmeticSymbolsPattern = /\*|\//g;
    
    const result = {};

    for (const p of participants) {
        let baseDmg = 0;
        let health = 0;
        
        if (healthPattern.test(p)) {
            for (const hm of p.match(healthPattern)) {
                health += hm.charCodeAt(0);
            }    
        }
        
        if (damagePattern.test(p)) {
            baseDmg = p
                .match(damagePattern)
                .map((el) => Number(el))
                .reduce(
                    (previousVal, currentVal) => previousVal + currentVal
                );
        }

        if (arithmeticSymbolsPattern.test(p)) {
            for (const op of p.match(arithmeticSymbolsPattern)) {
                if (op == '/') {
                    baseDmg /= 2;
                } else if (op == '*') {
                    baseDmg *= 2;
                }
            }
        }

        result[p] = [health, baseDmg];
    }

    const sortedResult = Object.entries(result).sort((a, b) => a[0].localeCompare(b[0]));
    for (const temp of sortedResult) {
        console.log(`${temp[0]} - ${temp[1][0]} health, ${temp[1][1].toFixed(2)} damage`);
    }
}

netherRealm('M3ph-0.5s-0.5t0.0**');
netherRealm('M3ph1st0**, Azazel');
// netherRealm('Gos/ho');
netherRealm('');
