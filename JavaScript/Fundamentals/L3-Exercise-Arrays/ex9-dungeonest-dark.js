function dungeon(dungeonsRooms) {
    let health = 100;
    let coins = 0;

    const HEALTH_MAX = 100;
    const COINS_MIN = 0;

    let rooms = dungeonsRooms[0].split('|');
    let questComplete = true;

    let i = 0;
    for (; i < rooms.length; i++) {
        let room = rooms[i];
        let roomData = room.split(' ');
        
        let roomType = roomData[0];
        let roomValue = Number(roomData[1]);

        if (roomType == 'potion') {
            let sum = health + roomValue;
            
            console.log(`You healed for ${sum > HEALTH_MAX 
                ? HEALTH_MAX - health
                : roomValue} hp.`);

            if (sum > HEALTH_MAX) {
                health = HEALTH_MAX;
            } else {
                health = sum;
            }
            
            console.log(`Current health: ${health} hp.`);

        } else if (roomType == 'chest') {
            coins += roomValue;
            if (coins < COINS_MIN) {
                coins = COINS_MIN;
            }
            console.log(`You found ${roomValue} coins.`);

        } else {
            health -= roomValue;
            if (health <= 0) {
                questComplete = false;
                health = 0;
                console.log(`You died! Killed by ${roomType}.`);
                console.log(`Best room: ${i + 1}`);
                break;
            }
            
            console.log(`You slayed ${roomType}.`);
        } 
    }

    if (questComplete) {
        console.log(`You've made it!`);
        console.log(`Coins: ${coins}`);
        console.log(`Health: ${health}`);
    }
}

dungeon(["rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000"]);
// dungeon(["cat 10|potion 30|orc 10|chest 10|snake 25|chest 110"]);
