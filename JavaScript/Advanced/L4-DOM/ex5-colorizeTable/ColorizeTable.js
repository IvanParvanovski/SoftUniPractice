function colorize() {
    const rows = document.querySelectorAll('table tr');
   
    for (let i = 0; i < rows.length; i++) {
        let currentRow = rows[i];

        if (i % 2 != 0) {
            currentRow.style.backgroundColor = 'teal';
        }
    }
}

// function colorize() {
//     const rows = document.querySelectorAll('table tr:nth-child(odd)');
    
//     for (const row of rows) {
//         row.style.backgroundColor = 'teal';
//     }
    
// }