function attachEvents() {
    const textareaElement = document.getElementById('messages');
    const authorElement = document.querySelector('input[name="author"]');
    const contentElement = document.querySelector('input[name="content"');

    document.getElementById('refresh').addEventListener('click', displayMessages);
    document.getElementById('submit').addEventListener('click', createMessage);

    displayMessages();

    async function displayMessages(event) {
        const url = 'http://localhost:3030/jsonstore/messenger';
        textareaElement.value = '';

        const response = await fetch(url);
        if (response.status != 200) {
            throw new Error(`${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        textareaElement.value = Object.values(data).map(v => `${v.author}: ${v.content}`).join('\n');        ;
    }
    
    async function createMessage(event) {
        const url = 'http://localhost:3030/jsonstore/messenger';

        const record = {
            author: authorElement.value,
            content: contentElement.value,
        };

        try {
            const response = await fetch(url, {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(record)
            });
    
            if (response.ok == false) {
                throw new Error(`${response.status} ${response.statusText}`);
            }
            
            authorElement.value = '';
            contentElement.value = '';
        } catch (error) {
            alert(error);
        }
    }
}

attachEvents();