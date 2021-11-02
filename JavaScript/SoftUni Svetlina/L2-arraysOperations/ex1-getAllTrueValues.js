const param = [true, false, true];

function getTrue() {
    return param.filter(x => x == true).length;
}

console.log(getTrue());
