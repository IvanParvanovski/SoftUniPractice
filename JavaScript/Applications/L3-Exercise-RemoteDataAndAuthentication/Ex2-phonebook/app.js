function attachEvents() {
    document.getElementById('btnLoad').addEventListener('click', displayPhoneNumbers);
    document.getElementById('btnCreate').addEventListener('click', createPhoneNumber);

    displayPhoneNumbers();
}

async function displayPhoneNumbers(event) {
    const listToAttachTo = document.getElementById('phonebook');
    listToAttachTo.replaceChildren();

    try {
        const phoneNumbers = await getPhoneNumbers();

        for (const [id, phoneNumber] of Object.entries(phoneNumbers)) {
            const li = document.createElement('li')
            li.textContent = `${phoneNumber.person}: ${phoneNumber.phone}`;
            
            const deleteBtn = document.createElement('button');
            deleteBtn.addEventListener('click', deleteEntry.bind(null, id));
            deleteBtn.textContent = 'Delete';
            
            li.appendChild(deleteBtn);
            listToAttachTo.appendChild(li);
        }
    } catch (err) {
        alert(err);
    }
}

function createPhoneNumber(event) {
    try {
        postPhoneNumber({
            person: document.getElementById('person').value,
            phone: document.getElementById('phone').value
        });
    } catch (err) {
        alert(err);
    }
}

function deleteEntry(id, event) {
    deletePhoneNumber(id);
    event.target.parentElement.remove();
}

async function getPhoneNumbers() {
    const url = 'http://localhost:3030/jsonstore/phonebook';

    const response = await fetch(url);
    
    if (response.status != 200) {
        throw new Error('Get Request Failed!');
    }

    return response.json();
}

async function postPhoneNumber(data) {
    const response = await fetch('http://localhost:3030/jsonstore/phonebook/', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    if (response.status != 200) {
        throw new Error(`${response.status} ${response.statusText}`);
    }

    return await response.json();
}

async function deletePhoneNumber(id) {
    fetch('http://localhost:3030/jsonstore/phonebook/' + id, {
        method: 'delete'
    });
}

attachEvents();