function heroicInventory(input) {
    function heroFactory(data) {
        const hero = {
            name: data[0],
            level: Number(data[1]),
            items: data[2] ? data[2].split(', ') : [],
        }

        return hero;
    }

    let heros = [];
    for (const heroData of input) {
        const heroTokens = heroData.split(' / ');
        heros.push(heroFactory(heroTokens));
    }

    return JSON.stringify(heros);
}

console.log(heroicInventory(['Isacc / 25 / Apple, GravityGun',
'Derek / 12 / BarrelVest, DestructionSword',
'Hes / 1 / Desolator, Sentinel, Antara']));
