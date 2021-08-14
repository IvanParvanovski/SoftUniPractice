function solve(input) {
    let people = {};

    for (let commandData of input) {
        let commandTokens = commandData.split(':');
        let command = commandTokens.shift();

        if (command == 'Result') {
            break;
        }

        if (command == 'Add') {
            let [personName, health, energy] = commandTokens; 
            health = Number(health);
            energy = Number(energy);

            if (!(personName in people)) {
                people[personName] = {
                    health: 0,
                    energy: energy,
                };
            }

            people[personName].health += health;

        } else if (command == 'Attack') {
            let [attackerName, deffenderName, damage] = commandTokens;
            damage = Number(damage);

            if (attackerName in people && deffenderName in people) {
                people[attackerName].energy -= 1;
                people[deffenderName].health -= damage;

                if (people[deffenderName].health <= 0) {
                    delete people[deffenderName];
                    console.log(`${deffenderName} was disqualified!`);
                } 
                
                if (people[attackerName].energy <= 0) {
                    delete people[attackerName];
                    console.log(`${attackerName} was disqualified!`);
                }
            }

        } else if (command == 'Delete') {
            let username = commandTokens[0];

            if (username == 'All') {
                people = {};
            } else {
                if (username in people) {
                    delete people[username];
                }
            }
        }
    }

    console.log(`People count: ${Object.keys(people).length}`);

    let sortedPeople = Object.entries(people).sort((a, b) => {
        if (a[1].health > b[1].health) {
            return -1;
        } else if (a[1].health < b[1].health) {
            return 1;
        }

        return a[0].localeCompare(b[0]);
    })

    for (let person of sortedPeople) {
        console.log(`${person[0]} - ${person[1].health} - ${person[1].energy}`);
    }
}

solve(["Add:Bonnie:3000:5",
"Add:Johny:4000:10",
"Delete:All",
"Add:Bonnie:3333:3",
"Add:Aleks:1000:70",
"Add:Tom:4000:1",
"Results"]);
