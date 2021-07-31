function phoneBook1(input) {
    let peopleNumbers = new Map();

    for (let personInfo of input) {
        let personData = personInfo.split(' ');
        
        peopleNumbers.set(personData[0], personData[1]);
    }

    for (let person of peopleNumbers) {
        console.log(`${person[0]} -> ${person[1]}`);
    }
}

function phoneBook2(input) {
    let peopleNumbers = {};

    for (let personInfo of input) {
        let personData = personInfo.split(' ');
        
        peopleNumbers[personData[0]] = personData[1];
    }

    for (let person of Object.entries(peopleNumbers)) {
        console.log(`${person[0]} -> ${person[1]}`);
    }
}

phoneBook1(['Tim 0834212554',
'Peter 0877547887',
'Bill 0896543112',
'Tim 0876566344']);
