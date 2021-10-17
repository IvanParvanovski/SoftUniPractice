function encodeAndDecodeMessages() {
    document.getElementById('main').addEventListener('click', encodeDecode);

    function codec(text, operation) {
        const operations = {
            encode: (x) => x.charCodeAt(0) + 1,
            decode: (x) => x.charCodeAt(0) - 1,
        };

        const result = [];

        for (const char of text) {
            result.push(String.fromCharCode(operations[operation](char)));
        }

        return result.join('');
    }

    function encodeDecode(event) {
        if (event.target.tagName !== 'BUTTON') {
            return;
        }

        const textareas = document.getElementsByTagName('textarea');
        let currentTextarea;
        let textareaToSet;

        if (event.target.textContent.toLowerCase().includes('encode')) {
            currentTextarea = textareas[0];
            textareaToSet = textareas[1];
            setTextarea(currentTextarea, 'encode', textareaToSet);

        } else if (event.target.textContent.toLowerCase().includes('decode')) {
            currentTextarea = textareas[1];
            textareaToSet = textareas[0];
            setTextarea(currentTextarea, 'decode', currentTextarea);
        }
    }

    function setTextarea(currentTextarea, operation, textareaToSet) {
        const textareaText = currentTextarea.value;
        currentTextarea.value = '';
        
        const encryptedText = codec(textareaText, operation);
        textareaToSet.value = encryptedText;
    }
}