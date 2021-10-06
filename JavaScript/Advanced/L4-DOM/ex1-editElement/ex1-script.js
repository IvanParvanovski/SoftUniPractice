/**
 * @param {HTMLElement} element 
 * @param {*} match 
 * @param {*} replacer 
 */
function edit(element, match, replacer) {
    const text = element.textContent;
    element.textContent = text.replaceAll(match, replacer);;
}