function totalVolume(...boxes) {
    console.log(boxes.reduce(
        (total, currentVal) => total + currentVal[0] * currentVal[1] * currentVal[2],
        0
    ));
}

totalVolume([4,2,4], [3,3,3], [1,1,2], [2,1,1]);
totalVolume([2,2,2], [2,1,1]);
totalVolume([1, 1, 1]);