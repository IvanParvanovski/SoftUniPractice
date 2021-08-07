function partyTime(input) {    
    function isDigit(char) {
        return char >= '0' && char <= '9';
    }

    let partyIndex = input.indexOf('PARTY');
    let reservationList = {
        vip: [],
        regular: [],
    }

    for (let i = 0; i < partyIndex; i++) {
        let currentGuest = input[i];

        if (isDigit(currentGuest[0])) {
            reservationList.vip.push(currentGuest);
        } else {
            reservationList.regular.push(currentGuest);
        }
    }

    for (let i = partyIndex + 1; i < input.length; i++) {
        let currentGuest = input[i];

        if (reservationList.vip.includes(currentGuest)) {
            reservationList.vip.splice(
                reservationList.vip.indexOf(currentGuest), 1
            );
        } else if (reservationList.regular.includes(currentGuest)) {
            reservationList.regular.splice(
                reservationList.regular
                .indexOf(currentGuest), 1
            );
        }
    }

    console.log(reservationList.vip.length + reservationList.regular.length);

    for (let guest of reservationList.vip) {
        console.log(guest);
    }

    for (let guest of reservationList.regular) {
        console.log(guest);
    }
}

partyTime(['7IK9Yo0h',
'9NoBUajQ',
'Ce8vwPmE',
'SVQXQCbc',
'tSzE5t0p',
'PARTY',
'9NoBUajQ',
'Ce8vwPmE',
'SVQXQCbc'
]);

// partyTime(['m8rfQBvl',
// 'fc1oZCE0',
// 'UgffRkOn',
// '7ugX7bm0',
// '9CQBGUeJ',
// '2FQZT3uC',
// 'dziNz78I',
// 'mdSGyQCJ',
// 'LjcVpmDL',
// 'fPXNHpm1',
// 'HTTbwRmM',
// 'B5yTkMQi',
// '8N0FThqG',
// 'xys2FYzn',
// 'MDzcM9ZK',
// 'PARTY',
// '2FQZT3uC',
// 'dziNz78I',
// 'mdSGyQCJ',
// 'LjcVpmDL',
// 'fPXNHpm1',
// 'HTTbwRmM',
// 'B5yTkMQi',
// '8N0FThqG',
// 'm8rfQBvl',
// 'fc1oZCE0',
// 'UgffRkOn',
// '7ugX7bm0',
// '9CQBGUeJ'
// ]);
