function solution() {
    const inputField = document.querySelector('input');
    const inputBtn = document.getElementById('registerButton');

    const parcelsList = document
        .getElementsByClassName('card')[1]
        .children[1];

    const parcelsSent = document
        .getElementsByClassName('card')[2]
        .children[1];

    inputBtn.addEventListener('click', (ev) => onRegister(ev));
    
    function onRegister(event) {
        if (inputField.value == '') {
            return;
        }

        const li = document.createElement('li');
        
        li.textContent = inputField.value;

        const btn = document.createElement('button');
        btn.textContent = 'Send';
        btn.addEventListener('click', (ev) => onSend(ev));

        li.appendChild(btn);
        
        parcelsList.appendChild(li);
        inputField.textContent = '';

        sortElements();
    }

    function sortElements() {
        const sortedElements = [...parcelsList.childNodes].sort(
            (a, b) => a.textContent.localeCompare(b.textContent)
        );

        for (const i of parcelsList.children) {
            i.remove();
        }

        for (const i of sortedElements) {
            parcelsList.appendChild(i);
        }
    }

    function onSend(event) {
        const clickedItem = event.target.parentNode;
        
        parcelsSent.appendChild(clickedItem);
        clickedItem.children[0].remove();
    }
}

