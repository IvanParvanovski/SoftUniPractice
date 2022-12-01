function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick)
   const tableRows = document.querySelectorAll('.container tbody tr');
   const inputField = document.getElementById('searchField');

   function onClick() {
      const searchedContent = inputField.value.replace(/\s+/g, '').toLowerCase();

      for (const tr of tableRows) {
         const content = tr.textContent.replace(/\s+/g, '').toLowerCase();
         
         if (content.includes(searchedContent)) {
            tr.className = 'select'
         } else {
            tr.className = '';
         }
      }

      inputField.textContent = '';
   }
}