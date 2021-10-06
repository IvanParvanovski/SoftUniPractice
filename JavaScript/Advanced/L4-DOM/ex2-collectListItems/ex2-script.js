/**
 * @param {HTMLCollection} items 
 */

function collectListItems(items, textArea) {
    let result = [];
    for (let item of Array.from(items)) {
        result.push(item.textContent);
    }
    
    textArea.value = result.join('\n');
}