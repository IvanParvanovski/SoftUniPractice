function sortArray(arr) {
    arr.sort((a, b) => b.length - a.length);
    console.log(arr.join(' '));
}

sortArray(['hi', '123', 'name']);
