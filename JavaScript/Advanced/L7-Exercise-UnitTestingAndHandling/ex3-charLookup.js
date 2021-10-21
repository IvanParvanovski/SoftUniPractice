// function lookupChar(string, index) {
//     if (typeof(string) != 'string' || isNaN(index)) {
//         return undefined;
//     }

//     if (index < 0 || index >= string.length) {
//         return "Incorrect index";
//     }

//     return string[index];
// }

function lookupChar(string, index) {
    if (typeof(string) !== 'string' || !Number.isInteger(index)) {
        return undefined;
    }
    if (string.length <= index || index < 0) {
        return "Incorrect index";
    }

    return string.charAt(index);
}

module.exports = {
    lookupChar,
};
