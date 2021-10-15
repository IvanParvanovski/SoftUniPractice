function deleteByEmail() {
    const tableBodyElement = document.querySelector('table tbody');
    const searchedEmailElement = document.querySelector('input[name="email"]');

    const searchedEmail = searchedEmailElement.value;
    searchedEmailElement.value = '';

    const rows = Array
        .from(tableBodyElement.children)
        .filter((r) => r.cells[1].textContent == searchedEmail)
        
    rows.forEach(r => r.remove());

    document.getElementById('result').textContent = rows.length == 0 ? 'Not found.' : 'Deleted.';
}

// function deleteByEmail() {
//     const tableBodyElement = document.querySelector('table tbody');
//     const searchedEmailElement = document.querySelector('input[name="email"]');

//     const searchedEmail = searchedEmailElement.value;
//     searchedEmailElement.value = '';

//     const rows = Array.from(tableBodyElement.children);
//     let deleted = false;

//     for (const row of rows) {
//         if (row.cells[1].textContent == searchedEmail) {
//             row.remove();
//             deleted = true;
//         } 
//     }

//     document.getElementById('result').textContent = deleted ? 'Deleted.' : 'Not found.';
// }