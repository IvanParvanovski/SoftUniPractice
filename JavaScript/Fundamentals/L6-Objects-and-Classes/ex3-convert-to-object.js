function convertToObject(jsonObject) {
    let result = JSON.parse(jsonObject);

    for (let key of Object.keys(result)) {
        console.log(`${key}: ${result[key]}`);
    }
}

json('{"name": "George", "age": 40, "town": "Sofia"}');