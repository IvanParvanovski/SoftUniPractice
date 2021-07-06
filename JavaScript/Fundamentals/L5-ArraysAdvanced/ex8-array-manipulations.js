function arrayManipulation(data) {
    function add(array, element) {
        array.push(element);
    }

    function remove(array, element) {
        return array.filter(x => x !== element);
    } 

    function removeAt(array, index) {
        array.splice(index, 1);
    }

    function insert(array, element, index) {
        array.splice(index, 0, element);
    }

    let array = data.shift().split(' ');
    
    while (data.length > 0) {
        let currentCommandData = data.shift().split(' ');
        let currentCommand = currentCommandData[0];
        let element = currentCommandData[1];

        switch (currentCommand) {
            case 'Add':
                add(array, element);
                break;
            case 'Remove':
                array = remove(array, element);
                break;
            case 'RemoveAt':
                removeAt(array, element)
                break;
            case 'Insert':
                let index = currentCommandData[2];
                insert(array, element, index);
                break;
        }
    }
    console.log(array.join(' '));
}

arrayManipulation(['4 19 2 53 6 43', 'Add 3', 'Remove 2', 'RemoveAt 1', 'Insert 8 3']);