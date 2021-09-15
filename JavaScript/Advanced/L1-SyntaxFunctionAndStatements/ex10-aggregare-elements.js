function operations(elements) {
    function sum(array) {
        let total = 0;

        for (let num of array) {
            total += num;
        }
        
        return total;
    }

    function partSum(array) {
        let total = 0;

        for (let num of array) {
            total += 1 / num;
        }

        return total;
    }

    function concat(array) {
        return array.join('');
    }

    console.log(sum(elements));
    console.log(partSum(elements));
    console.log(concat(elements));
}

operations([1, 2, 3])
