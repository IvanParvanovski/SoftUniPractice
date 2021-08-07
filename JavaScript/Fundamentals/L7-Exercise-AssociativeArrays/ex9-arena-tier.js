function arena(input) {
    function findObject(objects, searchedObjectAttribute) {
        // Searches an object by a given key
        return Object.entries(objects).find(o => o[0] == searchedObjectAttribute);
    }

    function calculateSharedGladiatorPoints(techniques, gladiator) {
        let total = 0;
        let gladiatorTechniques = gladiator[1];

        for (let techniqueName of techniques) {
            total += gladiatorTechniques[techniqueName];
        }

        return total;
    }

    function calculateGladiatorTotal(techniques) {
        let total = 0;

        for (let value of Object.values(techniques)) {
            total += value
        }    

        return total;
    }

    let gladiators = {};

    // Iterate until 'Ave Cesar' and
    // Add each gladiator to the gladiator pool
    
    for (let data of input) {
        if (data == 'Ave Cesar') {
            break;
        }

        // Check if there is a battle
        let dataTokens = data.split(' ');

        if (dataTokens.includes('vs')) {
            // If there is a battle, check if both gladiators exist
            
            let [firstGladiatorName, _, secondGladiatorName] = dataTokens;

            // If both gladiators exist and they have a shared technique, 
            // remove the one who has a lower value
            // If they don't have a shared technique, they both continue in the league

            let firstGladiator = findObject(gladiators, firstGladiatorName);
            let secondGladiator = findObject(gladiators, secondGladiatorName);

            if (
                typeof(firstGladiator) === 'undefined' ||
                typeof(secondGladiator) === 'undefined'
            ) {
                continue;
            }

            let firstGladiatorTechniques = Object.keys(firstGladiator[1]);
            let secondGladiatorTechniques = Object.keys(secondGladiator[1]);

            let sharedTechniques = firstGladiatorTechniques.filter(t => secondGladiatorTechniques.includes(t));

            // Check if the given gladiators have shared techniques
            
            if (sharedTechniques.length > 0) {
                let firstGladiatorPoints = calculateSharedGladiatorPoints(sharedTechniques, firstGladiator);
                let secondGladiatorPoints = calculateSharedGladiatorPoints(sharedTechniques, secondGladiator);

                if (firstGladiatorPoints < secondGladiatorPoints) {
                    delete gladiators[firstGladiatorName];
                } else {
                    delete gladiators[secondGladiatorName];
                }
            }
        } else {
            // Get gladiator's name, technique and skill value
                    
            let [gladiator, technique, skill] = data.split(' -> ');
            skill = Number(skill);

            // If the gladiator exists add only his technique.
            // Otherwise add the gladiator and his technique as well.

            if (!(gladiator in gladiators)) {
                gladiators[gladiator] = {};
            }

            // If the technique exists, compare the current 
            // technique's value and the new one's value and if the
            // new one's value is higher, set it to the higher value.

            if (technique in gladiators[gladiator]) {
                let currentValue = gladiators[gladiator][technique];

                if (skill > currentValue) {
                    gladiators[gladiator][technique] = skill;
                }
            } else {
                gladiators[gladiator][technique] = skill;
            }
        }
    }

    // Order the gladiators by their total skills in descending order and
    // Then ordered by name in ascending order

    let sortedGladiators = Object.entries(gladiators).sort((a, b) => {

        let firstGladiatorTotal = calculateGladiatorTotal(a[1]);
        let secondGladiatorTotal = calculateGladiatorTotal(b[1]);
        
        // Order by total skill
        if (firstGladiatorTotal < secondGladiatorTotal) {
            return 1;
        } else if (firstGladiatorTotal > secondGladiatorTotal) {
            return -1;
        } 

        // Order by name
        return a[0].localeCompare(b[0]);
    });

    for (let [gladiatorName, gladiatorTechniques] of sortedGladiators) {
        console.log(`${gladiatorName}: ${calculateGladiatorTotal(gladiatorTechniques)} skill`);

        let sortedTechniques = Object.entries(gladiatorTechniques).sort((a, b) => {
            // Order by skill value
            if (a[1] < b[1]) {
                return 1;
            } else if (a[1] > b[1]){
                return -1;
            }

            return a[0].localeCompare(b[0]);
        });

        for (let [skill, value] of sortedTechniques) {
            console.log(`- ${skill} <!> ${value}`);
        }
    }
}

arena([
    'Peter -> BattleCry -> 400',
    'Alex -> PowerPunch -> 300',
    'Stefan -> Duck -> 200',
    'Stefan -> Tiger -> 250',
    'Ave Cesar'
    ]);

console.log('----------------');

arena([
    'Pesho -> Duck -> 400',
    'Julius -> Shield -> 150',
    'Gladius -> Heal -> 200',
    'Gladius -> Support -> 250',
    'Gladius -> Shield -> 250',
    'Peter vs Gladius',
    'Gladius vs Julius',
    'Gladius vs Maximilian',
    'Ave Cesar'
    ]);
