function addItem() {
    const inputElement = document.getElementById('newItemText');
    const inputText = inputElement.value;
    inputElement.value = '';
    
    const liElement = document.createElement('li');
    liElement.textContent = inputText;

    document.getElementById('items').appendChild(liElement);
}