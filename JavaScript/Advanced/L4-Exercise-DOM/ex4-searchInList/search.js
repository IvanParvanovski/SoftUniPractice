function search() {
   const possibleTowns = Array.from(document.querySelectorAll('#towns li'));
   const searchedText = document.getElementById('searchText').value;
   const matchResult = document.getElementById('result');
   let matches = 0;

   for (const town of possibleTowns) {
      town.style.textDecoration = 'none';
      town.style.fontWeight = 'normal';
   }

   for (const town of possibleTowns) {
      const townLower = town.textContent.toLowerCase();
      const searchedTextLower = searchedText.toLowerCase();

      if (townLower.includes(searchedTextLower)) {
         town.style.textDecoration = 'underline';
         town.style.fontWeight = 'bold';
         matches++;
      } 
   }

   matchResult.textContent = `${matches} matches found`;
}

