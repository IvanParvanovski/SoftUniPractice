function checkIsMatch(firstString, symbol, wantedResult) {
    let result = firstString.replace('_', symbol);

    if (result == wantedResult) {
        console.log("Matched");
    } else {
        console.log("Not Matched");
    }
} 

checkIsMatch("Str_ng", 'I', 'String');