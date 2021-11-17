function totalVolume(...boxes) {
    return boxes.reduce(
        (total, currentVal) => total + currentVal[0] * currentVal[1] * currentVal[2],
        0
    );
}


console.log(totalVolume([4,2,4], [3,3,3], [1,1,2], [2,1,1]));

console.log(totalVolume([2,2,2], [2,1,1]));

console.log(totalVolume([1, 1, 1]));
