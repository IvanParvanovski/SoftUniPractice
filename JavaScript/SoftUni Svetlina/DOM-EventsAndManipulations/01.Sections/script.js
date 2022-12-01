function create(words) {
    const content = document.getElementById('content');

    for (const word of words) {
        const container = document.createElement('div');        
        const paragraph = document.createElement('p');
        
        paragraph.innerHTML = word;
        paragraph.style.display = 'none';

        container.appendChild(paragraph);
        content.appendChild(container);
        
        container.addEventListener('click', (ev) => onClick(ev));
    }

    function onClick(event) {
        const elements = event.target.children;
        
        if (elements.length == 0) {
            return;
        }

        if (elements[0].tagName == 'P') {
            const paragraph = elements[0];
            paragraph.style.display = 'inline-block'
        }
    }
}

