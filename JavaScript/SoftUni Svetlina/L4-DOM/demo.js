function solve() {
    const rows = [...document.querySelectorAll('tbody tr')];
    rows.pop();
    rows.shift();

    const sum = rows.reduce((total, currentValue) => {
        return total + Number(currentValue.cells[1].textContent);
    }, 0);

    const result = document.getElementById('sum');
    result.textContent = sum;
}