const obj = {
    a: 1, 
    b: 2
}

console.log(obj)
Object.defineProperty(obj, 'a', {value: 5, enumerable: true});

console.log(obj);
