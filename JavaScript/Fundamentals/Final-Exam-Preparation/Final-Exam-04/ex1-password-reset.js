function passwordReset(input) {
    let password = input.shift();

    for (let commandData of input) {
        let commandTokens = commandData.split(' ');
        let command = commandTokens[0];

        if (command == 'Done') {
            break;
        }

        switch (command) {
            case 'TakeOdd':
                let newString = [];
                // for (let [i, symbol] of Object.entries(password)) {
                //     if (i % 2 != 0) {
                //         newString.push(symbol);
                //     }
                // }

                for (let i = 1; i < password.length; i += 2) {
                    newString.push(password[i]);
                }
                
                password = newString.join('');

                console.log(password);
                break;
            case 'Cut':
                let startIndex = Number(commandTokens[1]);
                let length = Number(commandTokens[2]);
                
                let searchedString = password.substring(
                    startIndex,
                    startIndex + length
                );

                password = password.replace(searchedString, '');

                console.log(password);
                break;
            case 'Substitute':
                let searchedSubstring = commandTokens[1];
                let substituteString = commandTokens[2];
                
                let result = 'Nothing to replace!';
                
                if (password.includes(searchedSubstring)) {
                    let passwordTokens = password.split(searchedSubstring);
                    password = passwordTokens.join(substituteString);
                    result = password;    
                } 

                console.log(result);
                break;
        }
    }
    
    console.log(`Your password is: ${password}`);
}
