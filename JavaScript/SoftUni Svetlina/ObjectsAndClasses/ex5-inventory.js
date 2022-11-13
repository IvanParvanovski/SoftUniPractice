function inventory(input) {
    const heros = []

    for (const heroInfo of input) {
        const [name, level, items] = heroInfo.split(' / ');
        
        heros.push({
            name,
            level,
            items: items.split(', ').sort((a, b) => a.localeCompare(b))
        });
    }

    const sortedHeros = heros.sort((a, b) => a.level - b.level);
    for (const h of sortedHeros) {
        console.log([
            `Hero: ${h.name}`,
            `level => ${h.level}`,
            `items => ${h.items.join(', ')}`
        ].join('\n'));
    }
}

inventory([
    "Isacc / 25 / Apple, GravityGun",
    "Derek / 12 / BarrelVest, DestructionSword",
    "Hes / 1 / Desolator, Sentinel, Antara"
])
    
