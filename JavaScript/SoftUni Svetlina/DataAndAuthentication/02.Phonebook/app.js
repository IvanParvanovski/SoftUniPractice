function attachEvents() {
    const phoneBook = document.getElementById('phonebook');
    document.getElementById('btnLoad').addEventListener('click', onLoad);
    document.getElementById('btnCreate').addEventListener('click', onCreate);

    async function onLoad() {
        phoneBook.innerHTML = '';

        const phones = await (await fetch('http://localhost:3030/jsonstore/phonebook')).json();
        
        for (const phoneId in phones) {
            const li = document.createElement('li');
            const phone = phones[phoneId];
            li.setAttribute('phone-id', phone._id)  

            const btnDelete = document.createElement('button');
            btnDelete.addEventListener('click', onDelete);
            btnDelete.textContent = 'Delete';

            li.innerHTML = `${phone.person}:${phone.phone}`;
            li.appendChild(btnDelete);

            phoneBook.appendChild(li);
        }
    }

    async function onCreate() {
        const personInput = document.getElementById('person');
        const phoneInput = document.getElementById('phone');
    

        const response = await fetch('http://localhost:3030/jsonstore/phonebook', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({person: personInput.value, phone: phoneInput.value})
        });

        console.log(response);

        personInput.value = '';
        phoneInput.value = '';
    }

    async function onDelete(event) {
        const currentId = event.target.parentNode.getAttribute('phone-id');

        await fetch(`http://localhost:3030/jsonstore/phonebook/${currentId}`, {method: 'delete'});
        event.target.parentNode.remove();
    }

}

attachEvents();