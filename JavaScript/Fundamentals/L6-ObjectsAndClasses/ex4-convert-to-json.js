function convertToJson(name, lastName, hairColor) {
    let person = {
        name: name,
        lastName: lastName,
        hairColor: hairColor,
    };

    let jsonObject = JSON.stringify(person);
    console.log(jsonObject);
}

console.log(convertToJson('George', 'Jones', 'Brown'));
