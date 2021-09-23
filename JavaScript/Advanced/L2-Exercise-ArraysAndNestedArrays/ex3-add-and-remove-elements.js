function addAndRemoveElements(commands) {
    let number = 1; 
    let result = [];

    for (let command of commands) {
        // if (command == 'add') {
        //     result.push(number);
        // } else if (command == 'remove') {
        //     result.pop();
        // }

        command == 'add' ? result.push(number) : result.pop();
        number++;
    }

    console.log(result.length == 0 ? 'Empty' : result.join('\n'));
}


addAndRemoveElements(['add', 'add', 'remove']);
