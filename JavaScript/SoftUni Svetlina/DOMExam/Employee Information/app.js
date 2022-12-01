function deleteByID() {
    const rows = document.querySelectorAll('tbody tr');
    const inputField = document.querySelector('input[name="ID"]');
    const result = document.getElementById('result');

    function findElement() {
        for (const row of rows) {
            const rowId = row.children[2].textContent;
    
            if (rowId == inputField.value) {
                result.textContent = 'Deleted.';
                row.remove(); 
                return;
            }
        }

        result.textContent = 'Not found.'
    }   
    
    findElement();
}

