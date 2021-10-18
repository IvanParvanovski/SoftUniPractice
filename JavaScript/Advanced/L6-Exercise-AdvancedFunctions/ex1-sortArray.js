function sortArray(sequence, type) {
    function sortAscending() {
        return this.sequence.sort((a, b) => a - b);
    }

    function sortDescending() {
        return this.sequence.sort((a, b) => b - a);
    }

    const resultObj = {
        sequence,
        'asc': sortAscending,
        'desc': sortDescending,
    }

    return resultObj[type]();
}

sortArray([14, 7, 17, 6, 8], 'asc');
