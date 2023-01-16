class result {
    static multiply(arr, multiplier) {
        return arr.map(x => x * multiplier);
    }

    static multiswap(arr1, arr2) {
        const result = [];

        for (let i = 0; i < arr1.length; i++) {
            result.push(arr1[i] * arr2[arr2.length - i - 1]);
        }

        return result.reduce((a, b) => a - b);
    }

}

