function sortByTwoCriteria(input) {
    input.sort((a, b) => {
        if (a.length > b.length) {
            return 1;
        } else if (a.length < b.length) {
            return -1;
        }

        return a.localeCompare(b);
    });

    console.log(input.join('\n'));
}

// sortByTwoCriteria(['alpha', 'beta']);
// sortByTwoCriteria(['Isacc', 'Theodor', 'Jack', 'Harrison', 'George']);
sortByTwoCriteria(['test', 'Deny', 'omen', 'Default']);
