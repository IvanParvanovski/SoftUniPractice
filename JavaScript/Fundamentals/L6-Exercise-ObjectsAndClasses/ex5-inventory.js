function inventory(input) {
    let heros = [];

    for (let heroData of input) {
        let heroInformation = heroData.split(' / ');
        
        let hero = heroInformation[0];
        let level = Number(heroInformation[1]);
        let itemsData = heroInformation[2].split(', ');
        let items = itemsData.sort((a, b) => a.localeCompare(b)).join(', ');

        let heroObject = {
            hero,
            level,
            items,
        };

        heros.push(heroObject);
    }

    let sortedHeros = heros.sort((a, b) => a.level - b.level);

    for (let heroObject of sortedHeros) {
        for (let key in heroObject) {
            let isHero = false;
    
            if (key == 'hero') {
                isHero = true;
            } 
    
            console.log(
                `${isHero ? 'Hero' : key}` +
                `${isHero ? ':' : ' =>'} ` +
                `${heroObject[key]}`
            );
        }
    }
}

inventory([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara',
]);
