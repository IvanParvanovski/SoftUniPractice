function generateReport() {
    const checkboxes = document.querySelectorAll('th input[type="checkbox"]');
    const rows = document.querySelectorAll('tbody tr');
    const result = [];

    for (const row of rows) {
        const rowCells = row.cells;
        let personData = {};

        for (let i = 0; i < checkboxes.length; i++) {
            const currentCheckBoxElement = checkboxes[i];

            if (currentCheckBoxElement.checked) {
                personData[currentCheckBoxElement.getAttribute('name')] = rowCells[i].textContent;
            }
        }

        if (Object.keys(personData).length !== 0) {
            result.push(personData);
        }
    }

    document.getElementById('output').value = JSON.stringify(result);
}