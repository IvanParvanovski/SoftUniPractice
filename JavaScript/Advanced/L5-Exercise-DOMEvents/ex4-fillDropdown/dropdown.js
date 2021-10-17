function addItem() {
    const selectMenu = document.getElementById('menu');

    const newItemTextElement = document.getElementById('newItemText');
    const newItemText = newItemTextElement.value;
    newItemTextElement.value = '';

    const newItemValueElement = document.getElementById('newItemValue');
    const newItemValue = newItemValueElement.value;
    newItemValueElement.value = '';

    const newItem = document.createElement('option');
    newItem.textContent = newItemText;
    newItem.value = newItemValue;

    selectMenu.appendChild(newItem);
}