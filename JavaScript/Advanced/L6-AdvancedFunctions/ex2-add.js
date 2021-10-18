function solution(mainValue) {
    return (num) => num + mainValue; 
}

let add5 = solution(5);
console.log(add5(2));
console.log(add5(3));
