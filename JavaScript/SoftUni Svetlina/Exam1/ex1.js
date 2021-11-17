function numLayers(foldTimes) {
    return 0.0005 * Math.pow(2, Number(foldTimes)) + 'm';
}

// module.exports = { numLayers };

console.log(numLayers(1));

console.log(numLayers(2));

console.log(numLayers(4));

console.log(numLayers(21));
