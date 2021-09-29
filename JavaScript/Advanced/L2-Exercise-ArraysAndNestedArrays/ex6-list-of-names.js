function listOfNames(names) {
    let sortedNames = names.sort((a, b) => a.localeCompare(b));
    sortedNames.forEach((element, index) => {
        console.log(`${index + 1}.${element}`);
    });
}

listOfNames(['John', 'Bob', 'Christina', 'Ema']);
