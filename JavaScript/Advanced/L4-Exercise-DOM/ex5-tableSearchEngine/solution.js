function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const searchElement = document.getElementById('searchField');
      
      const searchedValue = searchElement.value.toLowerCase();
      const rows = document.querySelectorAll('tbody tr');

      for (const row of rows) {
         for (const col of row.children) {
            const elementTextLower = col.textContent.toLowerCase();

            if (elementTextLower.includes(searchedValue)) {
               row.classList.add('select');
               break;
            } else {
               row.classList.remove('select');
            }
         }
      }
      searchElement.value = '';
      
      console.log(rows[0].className);
   }
}
