function addItem() {
    function removeElement(event) {
        const parent = event.target.parentNode;
        parent.remove();
    }

    const listItems = document.getElementById('items');
    const inputElement = document.getElementById('newItemText');
    
    const newItem = document.createElement('li');
    newItem.textContent = inputElement.value;

    const newDeleteButton = document.createElement('a');
    newDeleteButton.textContent = '[Delete]';
    newDeleteButton.href = '#';
    newDeleteButton.addEventListener('click', removeElement);

    newItem.appendChild(newDeleteButton);
    listItems.appendChild(newItem);
}

