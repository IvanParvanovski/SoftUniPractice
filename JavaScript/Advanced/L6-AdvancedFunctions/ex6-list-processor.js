function solve(input) {
    let text = [];

    function add(string)  {
        text.push(string);
    }

    function remove(string) {
        while (text.includes(string)) {
            text.splice(text.indexOf(string), 1);
        }
    }

    function print() {
        console.log(text.join(','));
    }

    const commands = {
        add,
        remove,
        print,
    };

    for (let userCommand of input) {
        const [command, value] = userCommand.split(' ');
        commands[command](value);
    }
}

solve(['add pesho', 'add george', 'add peter', 'remove peter','print']);