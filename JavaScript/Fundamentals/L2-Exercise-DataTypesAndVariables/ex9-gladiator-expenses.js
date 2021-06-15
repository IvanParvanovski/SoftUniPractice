// function gladiator(lostFights, 
//                    helmetPrice,
//                    swordPrice,
//                    shieldPrice,
//                    armourPrice) {
    
//     let brokenHelmets = 0;
//     let brokenSwords = 0;
//     let brokenShields = 0;
//     let brokenArmours = 0;

//     let armoursCounter = 0;
    
//     for (let i = 1; i < lostFights + 1; i++) {
//         if (i % 2 == 0) {
//             brokenHelmets++;
//         } 
        
//         if (i % 3 == 0) {
//             brokenSwords++;
//         }

//         if (i % 2 == 0 && i % 3 == 0) {
//             brokenShields++;
//             armoursCounter++;
//         }

//         if (armoursCounter % 2 == 0 && armoursCounter != 0) {
//             brokenArmours++;
//             armoursCounter = 0;
//         }
//     }

//     let result = brokenHelmets * helmetPrice + 
//                  brokenSwords * swordPrice +
//                  brokenShields * shieldPrice +
//                  brokenArmours * armourPrice;
    
//     console.log(`Gladiator expenses: ${result.toFixed(2)} aureus`);
// }

function gladiator(lostFights, helmetPrice, swordPrice, shieldPrice, armourPrice) {
    let result = 0;

    for (let i = 1; i <= lostFights; i++) {
        if (i % 2 == 0) {
            result += helmetPrice;
        }

        if (i % 3 == 0) {
            result += swordPrice;
        }

        if (i % 6 == 0) {
            result += shieldPrice;
        }

        if (i % 12 == 0) {
            result += armourPrice;
        }
    }

    console.log(`Gladiator expenses: ${result.toFixed(2)} aureus`);
}

gladiator(5, 2, 3, 4, 5);
gladiator(7, 2, 3, 4, 5);
gladiator(23, 12.50, 21.50, 40, 200);
