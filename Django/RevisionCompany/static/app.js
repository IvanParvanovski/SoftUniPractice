function initExpand() {
    const items = [...document.getElementsByClassName('todoTitle')];

    for (let item of items) {
        item.addEventListener('click', expandCollapse)
    }
}

function expandCollapse(ev) {
    let element = this.nextElementSibling;

    if (element.style.display === 'none') {
        element.style.display = '';
    } else {
        element.style.display = 'none';
    }
}

console.log('hi');
initExpand()
