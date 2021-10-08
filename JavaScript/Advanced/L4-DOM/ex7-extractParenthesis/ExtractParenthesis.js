function extract(content) {
    let rawText = document.getElementById(content).textContent;

    let regexPattern = /\((\w+\s?)+\)/g;
    let regex = new RegExp(regexPattern);

    let result = []
    for (let match of rawText.match(regex)) {
        result.push(match.slice(1, match.length - 1));
    }

    let text = result.join('; ');
    return text;
}
