function dictionary(input) {
    const dict = {}

    for (const term of input) {
        const termObject = JSON.parse(term);
        dict[Object.keys(termObject)[0]] = Object.values(termObject)[0];
    }
    
    for (const term of Object.entries(dict).sort((a, b) => a[0].localeCompare(b[0]))) {
        console.log(`Term: ${term[0]} => Definition: ${term[1]}`);
    } 
}

dictionary([
    '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
    '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
    '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
    '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
    '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}'
    ]
);
