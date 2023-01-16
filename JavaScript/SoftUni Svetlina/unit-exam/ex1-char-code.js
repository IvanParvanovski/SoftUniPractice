function solve(arr, argument) {
    let result;

    if (argument == 'desc') {
        result = arr.sort((a, b) => b.charCodeAt(0) - a.charCodeAt(0));
    } else if (argument == 'asc') {
        result = arr.sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0));
    }

    console.log(result);
    return result;
}

solve(['a', 'n', 'k', 'd', 'c'],'desc');
solve(['a', 'n', 'k', 'd', 'c'],'asc');
