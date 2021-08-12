function matchFullName(names) {
    let pattern = /\b[A-Z][a-z]+ [A-Z][a-z]+\b/g;
    let result = [];
    
    let match = pattern.exec(names);
    while (match != null) {
        result.push(match[0]);

        match = pattern.exec(names);
    }
    console.log(result.join(' '));
}

matchFullName('123, Ivan Ivanov, Hi, Alek Andriqnov');