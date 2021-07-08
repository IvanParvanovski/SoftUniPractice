function houseParty(input) {
    let guests = [];

    for (let guestData of input) {
        let guestInfo = guestData.split(' ');
        let guestName = guestInfo.shift();
        let guestStatus = guestInfo.join(' ');

        if (guestStatus == 'is going!') {
            if (guests.includes(guestName)) {
                console.log(`${guestName} is already in the list!`);
            } else {
                guests.push(guestName);
            }
        } else {
            let guestIndex = guests.indexOf(guestName);

            if (guestIndex == -1) {
                console.log(`${guestName} is not in the list!`);
            } else {
                guests.splice(guestIndex, 1);
            }
        }
    }

    console.log(guests.join('\n'));
}

houseParty(['Allie is going!', 'George is going!', 'John is not going!', 'George is not going!']);
console.log('---');
houseParty(['Tom is going!', 'Annie is going!', 'Tom is going!', 'Garry is going!', 'Jerry is going!']);
