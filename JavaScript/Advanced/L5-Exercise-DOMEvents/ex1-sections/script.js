function create(words) {
   const resultDiv = document.getElementById('content');
   createElements(words);

   function createElements(elementNames) {
      for (const elementName of elementNames) {
         const divElement = document.createElement('div');
      
         const paragraphElement = document.createElement('p');
         paragraphElement.textContent = elementName;
         paragraphElement.style.display = 'none';
   
         divElement.appendChild(paragraphElement);
         divElement.addEventListener('click', onClick);

         resultDiv.appendChild(divElement);
      }
   }

   function onClick(event) {
      const clickedDiv = event.currentTarget;
      const paragraph = clickedDiv.children[0];
      paragraph.style.display = 'inline-block';
   }
}