function attachEvents() {
    const textArea = document.getElementById('messages');
    console.log(textArea);
    
    const authorInput = document.querySelector('input[name="author"]');
    const contentInput = document.querySelector('input[name="content"]');

    document.getElementById('submit').addEventListener('click', onSubmit);
    document.getElementById('refresh').addEventListener('click', onRefresh);

    async function onSubmit() {
        obj = {
            author: authorInput.value,
            content: contentInput.value
        };

        const response = await fetch(
            'http://localhost:3030/jsonstore/messenger', {
                 method: 'post', 
                 headers: { 'Content-Type': 'application/json', },
                 body: JSON.stringify(obj)
            });

        console.log(response)

    }

    async function onRefresh() {
        const result = await (await fetch('http://localhost:3030/jsonstore/messenger')).json();
        textArea.innerHTML = '';
    
        for (const objId in result) {
            const currentObj = result[objId];
            const text = `${currentObj.author}: ${currentObj.content}\n`;

            textArea.innerHTML += text;
            
        }
    }
}

attachEvents();