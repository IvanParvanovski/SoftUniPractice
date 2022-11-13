function race(input) {
    let names = input.shift().split(', ');
    let racers = {};

    let namePattern = /[A-Za-z]+/g;
    let digitsPattern = /\d/g;

    for (let racerData of input) {
        if (racerData == 'end of race') {
            break;
        }
        
        let name = racerData.match(namePattern).join('');
        
        let score = 0;
        racerData.match(digitsPattern).map(d => score += Number(d));

        if (names.includes(name)) { 
            if (!(name in racers)) {
                racers[name] = 0;
            }
            racers[name] += score;
        }
    }

    let sortedRacers = Object.entries(racers).sort((a, b) => b[1] - a[1]);

    console.log(`1st place: ${sortedRacers[0][0]}`);
    console.log(`2nd place: ${sortedRacers[1][0]}`);
    console.log(`3rd place: ${sortedRacers[2][0]}`);
}   

race([
    'George, Peter, Bill, Tom',
    "G4e@55or%6g6!68e!!@",
    "R1@!3a$y4456@",
    "B5@i@#123ll",
    "G@e54o$r6ge#",
    "7P%et^#e5346r",
    "T$o553m&6",
]);
