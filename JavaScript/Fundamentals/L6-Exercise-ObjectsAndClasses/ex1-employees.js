function employeeCard(people) {
    for (let person of people) {
        let employee = {
            name: person,
            personalCard: person.length,
        };

        console.log(`Name: ${employee.name} -- Personal Number: ${employee.personalCard}`);
    }
}

employeeCard([
    'Silas Butler',
    'Adnaan BUckley',
    'Juan Peterson',
    'Brendan Villarreal',
]);
