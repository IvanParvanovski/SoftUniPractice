function substring(text, startIndex, count) {
    console.log(text.substring(startIndex, startIndex + count));
}

let text = 'I am JavaScript developer';

substring(text.slice(), 5, 10);
substring(text.slice(), 10, 5);
substring(text.slice(), -5, 10);
substring(text.slice(), 5, -10);
substring(text.slice(), -5, -10);
