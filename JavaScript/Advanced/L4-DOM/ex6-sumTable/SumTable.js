function sumTable() {
    let resultElement = document.getElementById('sum');
    let rows = [...document.querySelectorAll('table tr')];
    rows.pop();
    
    let sum = 0;
    for (let i = 1; i < rows.length; i++) {
        sum += Number(rows[i].lastElementChild.textContent);
    }

    resultElement.textContent = sum;
}