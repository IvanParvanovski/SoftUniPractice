function partyTime(inputArray) {
    const reservationList = []; 
    let flag = false;

    for (const element of inputArray) {
        if (element == 'PARTY') {
            flag = true;
        }

        if (!flag) {
            reservationList.push(element);
        } else {
            if (reservationList.includes(element)) {
                reservationList.splice(reservationList.indexOf(element), 1)
            }
        }
    }

    let missingGuests = reservationList.sort((a, b) => a[0].charCodeAt(b[0], 0));
    
    console.log(missingGuests.length);

    for (const g of missingGuests) {
        console.log(g);
    }
}

partyTime(['7IK9Yo0h',
'7IK9Yo0h',
'7IK9Yo0h',
'9NoBUajQ',
'Ce8vwPmE',
'SVQXQCbc',
'tSzE5t0p',
'PARTY',
'9NoBUajQ',
'Ce8vwPmE',
'SVQXQCbc',
'7IK9Yo0h'
])


partyTime(['m8rfQBvl',
'fc1oZCE0',
'UgffRkOn',
'7ugX7bm0',
'9CQBGUeJ',
'2FQZT3uC',
'dziNz78I',
'mdSGyQCJ',
'LjcVpmDL',
'fPXNHpm1',
'HTTbwRmM',
'B5yTkMQi',
'8N0FThqG',
'xys2FYzn',
'MDzcM9ZK',
'PARTY',
'2FQZT3uC',
'dziNz78I',
'mdSGyQCJ',
'LjcVpmDL',
'fPXNHpm1',
'HTTbwRmM',
'B5yTkMQi',
'8N0FThqG',
'm8rfQBvl',
'fc1oZCE0',
'UgffRkOn',
'7ugX7bm0',
'9CQBGUeJ'
]);