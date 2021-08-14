function solve(input) {
    let pattern = /!(?<command>[A-Z][a-z]{2,})!:\[(?<text>[A-Za-z]{8,})]/;

    let amountOfCommands = Number(input.shift());

    for (let i = 0; i < amountOfCommands; i++) {
        let currentCommand = input[i];
        let commandData = pattern.exec(currentCommand);

        if (commandData != null) {
            let command = commandData.groups.command;
            let message = commandData.groups.text;
            
            let encryption = [];
            for (let symbol of message) {
                encryption.push(symbol.charCodeAt(0));
            }

            console.log(`${command}: ${encryption.join(' ')}`);
            
        } else {
            console.log('The message is invalid');
        }
    }
}

solve((["2",
"!Send!:[IvanisHere]",
"*Time@:[Itis5amAlready"]));
