function sum(num) {
    let total = num;

    function add(num2) {
        total += num2;

        return add;
    }

    add.toString = () => {
        return total;
    }

    return add; 
}

console.log(sum(1)(6)(-3).toString());
