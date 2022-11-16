function getValue() {
    return new Promise((res) => {
        setTimeout(() => {
            res('TEST');
        }, 2000)
    });
}


function getValue2(cb: (...args: any[]) => void) {
    setTimeout(()=> {
        cb('Test');
    }, 2000)
}

getValue2(function (value) {console.log(value); });
getValue().then(function (value) {console.log(value); });

