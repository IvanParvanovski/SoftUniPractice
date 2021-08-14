function solve(input) {
    function isInvalidIndex(sequence, index) {
        return index < 0 || index > sequence.length;
    }

    function replace(text, currentChar, newChar) {
        while (text.includes(currentChar)) {
            text = text.replace(currentChar, newChar);
        }

        return text;
    }

    function cut(text, startIndex, endIndex){
        if (isInvalidIndex(text, startIndex) || isInvalidIndex(text, endIndex)) {
            console.log('Invalid indices!');
        } else {
            let result = '';

            for (let i = 0; i < text.length; i++) {
                if (!(i >= startIndex && i <= endIndex)) {
                    result += text[i];
                }
            }

            console.log(result);
            return result;
        }

        return text;
    }

    function make(text, status) {
        if (status == 'Upper') {
            return text.toUpperCase();
        }
        return text.toLowerCase();
    }

    function check(text, string) {
        let result = text.includes(string);

        if (result) {
            return `Message contains ${string}`;
        } else {
            return `Message doesn't contain ${string}`;
        }

    }

    function sum(text, startIndex, endIndex) {
        if (isInvalidIndex(text, startIndex) || isInvalidIndex(text, endIndex)) {
            console.log('Invalid indices!');
        } else {
            let substringOfText = text.substring(startIndex, endIndex);

            let total = 0;
            for (let symbol of substringOfText) {
                total += symbol.charCodeAt(0);
            }

            console.log(total);
        }
    }

    let text = input.shift();

    for (let commandData of input) {
        let commandTokens = commandData.split(' ');
        let command = commandTokens[0];
        
        if (command == 'Finish') {
            break;
        }

        else if (command == 'Replace') {
            text = replace(text, commandTokens[1], commandTokens[2]);
            console.log(text);
        } else if (command == 'Cut') {
            text = cut(text, Number(commandTokens[1]), Number(commandTokens[2]));
        } else if (command == 'Make') {
            text = make(text, commandTokens[1]);
            console.log(text);
        } else if (command == 'Check') {
            console.log(check(text, commandTokens[1]));
        } else if (command == 'Sum') {
            sum(text, Number(commandTokens[1]), Number(commandTokens[2]) + 1);
        }
    }
}
solve([
    undefined,
    'Cut 0, 4',
]);

// solve(["ILikeSoftUni",
// "Replace I We",
// "Make Upper",
// "Check SoftUni",
// "Sum 1 4",
// "Cut 1 4",
// "Finish"]);

// solve(["HappyNameDay",
// "Replace p r",
// "Make Lower",
// "Cut 2 23",
// "Sum -2 2",
// "Finish"])