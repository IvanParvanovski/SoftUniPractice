function solve(input) {
    function findHero(heros, heroName) {
        return heros.find(h => h.name == heroName);
    }

    // Get the amount of heros
    let herosCount = Number(input.shift());
    
    // Store the heros
    let heros = [];

    // Iterate each hero and add him to the party
    for (let i = 0; i < herosCount; i++) {
        let heroTokens = input.shift().split(' ');
       
        let name = heroTokens[0];
        let health = Number(heroTokens[1]);
        let mana = Number(heroTokens[2]);        
        
        let hero = {
            name,
            health,
            mana,
        };

        heros.push(hero);
    }

    // Execute each command
    for (let commandData of input) {
        let commandTokens = commandData.split(' - ');
        let command = commandTokens.shift();

        // If receive 'End' the reading of commands should stop.
        if (command == 'End') {
            break;
        }

        // A message is always displayed.
        let message;       

        // Properties which are repeated
        let heroName = commandTokens[0];
        let hero = findHero(heros, heroName);

        switch (command) {
            // 'CastSpell - {hero name} - {MP needed} - {spell name}'
            case 'CastSpell':
                // If the hero has the needed mana he executes the spell
                // and his mana is reduced.

                // If the hero does not have the needed mana perfom 
                // the given action.
                
                let neededMana = Number(commandTokens[1]);
                let spellName = commandTokens[2];

                if (hero.mana - neededMana >= 0) {
                    hero.mana -= neededMana;

                    message = `${heroName} has successfully cast ${spellName} and now has ${hero.mana} MP!`;
                } else {
                    message = `${heroName} does not have enough MP to cast ${spellName}!`;
                }

                break;
                
            // 'TakeDamage - {hero name} - {damage} - {attacker}'
            case 'TakeDamage':
                // Reduce hero's health

                // If his health is less or equal to 0 he is dead and 
                // he should be removed from the party.

                // If his health is greater than 0 he continous in the party.
                
                let damage = Number(commandTokens[1]);
                let attacker = commandTokens[2];

                hero.health -= damage;

                if (hero.health <= 0) {
                    heros.splice(heros.indexOf(hero), 1);

                    message = `${heroName} has been killed by ${attacker}!`;
                } else {
                    message = `${heroName} was hit for ${damage} HP by ${attacker} and now has ${hero.health} HP left!`;
                }

                break;
            
            // 'Recharge - {hero name} - {amount}'
            case 'Recharge':
                // Hero's mana is increased, but the given maximum of 200 
                // shouldn't be exceeded.
                
                let maximumMana = 200;
                let manaAmount = Number(commandTokens[1]);
                
                let increasedMana = maximumMana - hero.mana;
                hero.mana += manaAmount;

                if (hero.mana > maximumMana) {
                    hero.mana = maximumMana;
                } else {
                    increasedMana = manaAmount
                }
                
                message = `${heroName} recharged for ${increasedMana} MP!`;
                break;

            // 'Heal - {hero name} - {amount}'
            case 'Heal':
                // Hero's health is increased, but the given maximum of 100
                // shouldn't be exceeded.
                
                let maximumHealth = 100;
                let healthAmount = Number(commandTokens[1]);

                let increasedHealth = maximumHealth - hero.health;
                hero.health += healthAmount;

                if (hero.health > maximumHealth) {
                    hero.health = maximumHealth;
                }  else {
                    increasedHealth = healthAmount;
                }

                message = `${heroName} healed for ${increasedHealth} HP!`
                break;
        }

        console.log(message);    
    }

    // Sort the heros by their health in descending and
    // their names in ascending order.
    let sortedHeros = heros.sort((a, b) => {
        if (a.health > b.health) {
            return -1
        } else if (a.health < b.health) {
            return 1;
        }

        return a.name.localeCompare(b.name);
    });

    // Display each hero
    for (let hero of sortedHeros) {
        console.log(hero.name);
        console.log(` HP: ${hero.health}`);
        console.log(` MP: ${hero.mana}`);
    }
}

solve([2,
    'Solmyr 85 120',
    'Kyrre 99 50',
    'Heal - Solmyr - 10',
    'Recharge - Solmyr - 50',
    'TakeDamage - Kyrre - 66 - Orc',
    'CastSpell - Kyrre - 15 - ViewEarth',
    'End']);

// solve([
// 4,
// 'Adela 90 150',
// 'SirMullich 70 40',
// 'Ivor 1 111',
// 'Tyris 94 61',
// 'Heal - SirMullich - 50',
// 'Recharge - Adela - 100',
// 'CastSpell - Tyris - 1000 - Fireball',
// 'TakeDamage - Tyris - 99 - Fireball',
// 'TakeDamage - Ivor - 3 - Mosquito',
// 'End'
// ])

