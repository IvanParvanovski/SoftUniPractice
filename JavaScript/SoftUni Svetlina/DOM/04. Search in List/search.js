function search() {
   const towns = document.querySelectorAll('#towns li');   
   const inputField = document.getElementById('searchText');
   let matches = 0;

   for (const town of towns) {
      if (town.textContent.toLowerCase().includes(inputField.value.toLowerCase())) {
         town.style.textDecoration = 'underline'
         town.style.fontWeight = 'bold';
         matches += 1;
      } else {
         town.style.textDecoration = '';
         town.style.fontWeight = '';
      }
   }

   document.getElementById('result').textContent = `${matches} matches found`;
}
