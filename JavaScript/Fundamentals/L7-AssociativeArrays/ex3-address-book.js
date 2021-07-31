function addressBook(input) {
    let peopleAddresses = new Map();

    for (let personData of input) {
        let personInfo = personData.split(':');
        
        peopleAddresses.set(personInfo[0], personInfo[1]);
    }

    let sortedPeople = [...peopleAddresses.entries()]
        .sort((a, b) => a[0]
        .localeCompare(b[0]));
        
    for (let person of sortedPeople) {
        console.log(`${person[0]} -> ${person[1]}`);
    }
}

addressBook([
    'Tim:Doe Crossing',
    'Bill:Nelson Place',
    'Peter:Carlyle Ave',
    'Bill:Ornery Rd'
]);
