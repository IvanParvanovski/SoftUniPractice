function averageStringsData(firstString, secondString, thirdString) {
    let totalLength = firstString.length + secondString.length + thirdString.length;
    let averageLength = totalLength / 3;

    console.log(totalLength);
    console.log(Math.floor(averageLength));
}

averageStringsData('chocolate', 'ice cream', 'cake');
