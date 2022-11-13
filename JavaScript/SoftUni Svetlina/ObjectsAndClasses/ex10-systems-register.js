function systemsRegister(input) {
    let database = {};

    for (const data of input) {
        const [system, component, subcomponent] = data.split(' | ');
        
        if (!(system in database)) {
            database[system] = [];
        }

        if (!database[system].find((el) => el.name == component)) {
            database[system].push({
                name: component,
                subcomponents: []
            })
        }

        const systemComponent = database[system].find((el) => el.name == component);
        systemComponent.subcomponents.push(subcomponent);
    }

    const sortedDB = Object.entries(database).sort((a, b) => {
        let res = a[1].length - b[1].length;

        if (res > 0) {
            return -1;
        } else if (res < 0) {
            return 1;
        }
        
        return a[0].localeCompare(b[0]);
    });


    for (const sys of sortedDB) {
        console.log(sys[0]);

        const sortedComponents = sys[1].sort((a, b) => b.subcomponents.length - a.subcomponents.length);
        
        for (const comp of sortedComponents) {
            console.log('|||' + comp.name);

            for (const subcomp of comp.subcomponents) {
                console.log('||||||' + subcomp);
            }
        }
    }
}

systemsRegister([
    'SULS | Main Site | Home Page ',
'SULS | Main Site | Login Page ',
'SULS | Main Site | Register Page ',
'SULS | Judge Site | Login Page ',
'SULS | Judge Site | Submittion Page ',
'Lambda | CoreA | A23 ',
'SULS | Digital Site | Login Page ',
'Lambda | CoreB | B24 ',
'Lambda | CoreA | A24 ',
'Lambda | CoreA | A25 ',
'Lambda | CoreC | C4 ',
'Indice | Session | Default Storage ',
'Indice | Session | Default Security'
])
