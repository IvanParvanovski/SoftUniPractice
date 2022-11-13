function starEnigma(input) {
    const msgCount = Number(input.shift());

    const letterRegex = /s|t|a|r/gi;
    const messageRegex = /@(?<name>[A-Za-z]+)[^@:!\->]*:(?<population>\d+)[^@:!\->]*!(?<status>[A|D])![^@:!\->]*\->(?<soldiers>\d+)/;

    const planets = {
        A: [],
        D: [],
    };

    for (let i = 0; i < msgCount; i++) {
        const msg = input[i];

        const keyMatch = msg.match(letterRegex);
        let key = 0;
        
        if (keyMatch) {
            key = keyMatch.length;
        }

        const newMsg = [];
        for (const letter of msg) {
            newMsg.push(String.fromCharCode((letter.charCodeAt(0) - key)));
        }
        
        const planetInfo = messageRegex.exec(newMsg.join(''));
        
        if (planetInfo){
            planets[planetInfo.groups.status].push(planetInfo.groups.name);
        }
    }
        
    console.log(`Attacked planets: ${planets.A.length}`);
    for (const attackedName of planets.A.sort((a, b) => a.localeCompare(b))) {
        console.log(`-> ${attackedName}`);
    }

    console.log(`Destroyed planets: ${planets.D.length}`);
    for (const destroyedName of planets.D.sort((a, b) => a.localeCompare(b))) {
        console.log(`-> ${destroyedName}`);
    }
}

starEnigma([
    "4", 
    "STCDoghudd4=63333$D$0A53333", 
    '',
    "EHfsytsnhf?8555&I&2C9555SR",
    'adsfdf;qioeur'
]);

// starEnigma([
//     "3", 
//     "tt(''DGsvywgerx>6444444444%H%1B9444",
//     "GQhrr|A977777(H(TTTT", 
//     "EHfsytsnhf?8555&I&2C9555SR"
// ]);

