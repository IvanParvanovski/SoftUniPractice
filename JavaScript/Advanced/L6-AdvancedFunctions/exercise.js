function solve(input) {
    const cars = {};

    function create(name) {
        cars[name] = {};
    }

    function inherit(name, parentName) {
        create(name);
        cars[name][parentName] = Object.entries(cars).find((c) => c[0] == parentName)[1];
    }

    function set(name, key, value) {
        cars[name][key] = value;
    }

    // [ [ c1: { color: 'red' } ], [ model: 'new' ] ]
    function getSpecs(result, object) {
        const currentSpec = Object.entries(object.shift())[0];
    
        if (typeof(currentSpec[1]) == 'object') {
            result.push(getSpecs([], [currentSpec[1]]));
        } else {
            result.push(currentSpec.join(':'));
        }    
    
        if (object.length == 0) {
            return result.join(',');
        }
    
        return getSpecs(result, object);
    }

    function print(name) {
        const searchedCar = Object.entries(cars).find((c) => c[0] == name);
        console.log(getSpecs([], [searchedCar]));
    }

    const commands = {
        create,
        inherit,
        set,
        print,
    }

    for (const commandInfo of input) {
        const commandTokens = commandInfo.split(' ');
        let command = commandTokens.shift();
        
        if (commandTokens.includes('inherit')) {
            command = 'inherit';
            commandTokens.splice(1, 1);
        }

        commands[command](...commandTokens);
    }
}



// [ c1: [ color: 'red' ], ]

solve(['create c1',
'create c2 inherit c1',
'set c1 color red',
'set c2 model new',
'print c1',
'print c2'
]);
