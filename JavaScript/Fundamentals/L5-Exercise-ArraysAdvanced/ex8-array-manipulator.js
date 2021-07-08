function arrayManipulator(numbers, commandsArray) {
    function add(array, index, element) {
        array.splice(index, 0, element);
    }

    function addMany(array, index, elements) {
        for (let element of elements) {
            array.splice(index, 0, element);
            index++;
        }
    }

    function contains(array, element) {
        return array.indexOf(element);
    }

    function remove(array, index) {
        array.splice(index, 1);
    }

    function shift(array, positions) {
        for (let i = 0; i < positions; i++) {
            array.push(array.shift());
        }
    }

    function sumPairs(array) {
        let result = [];

        while (array.length > 0) {
            let firstElement = array.shift();
            let secondElement = 0;

            if (array.length != 0) {
                secondElement = array.shift();;
            }

            result.push(firstElement + secondElement);
        }

        return result;
    }

    function print(array) {
        console.log(`[ ${array.join(', ')} ]`);
    }

    while (commandsArray.length > 0) {
        let rawCommand = commandsArray.shift();
        let commandData = rawCommand.split(' ');
        
        let command = commandData[0];
        
        switch(command) {
            case 'add':
                let currentIndex = Number(commandData[1]);
                let element = Number(commandData[2]);
                add(numbers, currentIndex, element);
                break;

            case 'addMany':
                let addMany_index = Number(commandData[1]); 
                let elements = commandData
                    .splice(2, commandData.length - 2)
                    .map(x => Number(x));

                addMany(numbers, addMany_index, elements)
                break;

            case 'contains':
                let currentElement = Number(commandData[1]);
                console.log(contains(numbers, currentElement));
                break;

            case 'remove':
                let index = Number(commandData[1]);
                remove(numbers, index);
                break;

            case 'shift':
                let positions = Number(commandData[1]);
                shift(numbers, positions);
                break;

            case 'sumPairs':
                numbers = sumPairs(numbers);
                break;

            case 'print':
                print(numbers);
                break;
        }

        if (command == 'print') {
            break;
        }
    }

}   

arrayManipulator([1, 2, 3, 4, 6], ['sumPairs', 'print']);
// arrayManipulator([1, 2, 4, 5, 6, 7], ['add 1 8', 'contains 1', 'contains 3', 'print']);
// arrayManipulator([1, 2, 3, 4, 5], ['addMany 5 9 8 7 6 5', 'contains 15', 'remove 3', 'shift 1', 'print']);