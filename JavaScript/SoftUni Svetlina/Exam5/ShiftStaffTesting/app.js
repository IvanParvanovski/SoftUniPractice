function attachEvents() {
    document.getElementById('btnLoad').addEventListener('click', getStaff)
    document.getElementById('btnAdd').addEventListener('click', () => {
        const person = document.getElementById('person').value;

        postStaff({ person });
        document.getElementById('person').value = '';
    })
    document.querySelector('table').addEventListener('click', staffDelete)
}

attachEvents();

async function request(url, options) {
    const response = await fetch(url, options);
    if (!response.ok) {
        const error = await response.json();
        alert(error.message);
        throw new Error(error.message);
    }
    const data = await response.json();
    return data;
}

async function getStaff() {
    document.getElementById('staff').innerHTML = ''
    const response = await fetch('http://localhost:3030/jsonstore/shift');
    const data = await response.json();

    const personData = Object.values(data).map(p => {
        const tr = document.createElement('tr');
        const tdPerson = document.createElement('td');
        const tdBtn = document.createElement('td');

        tdPerson.setAttribute('data-id', p._id)
        tdPerson.textContent = `${p.person}`;

        const btn = document.createElement('button');
        btn.textContent = 'Delete'
        btn.setAttribute('data-id', p._id)

        tdBtn.appendChild(btn)
        tr.appendChild(tdPerson)
        tr.appendChild(tdBtn)

        document.getElementById('staff').appendChild(tr)
    })
}

async function postStaff(data) {
    const response = await fetch('http://localhost:3030/jsonstore/shift', {
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
}

async function deleteStaffData(id) {
    const result = await request('http://localhost:3030/jsonstore/shift/' + id, {
        method: 'delete'
    });
    getStaff()

}

function staffDelete(event) {
    if (event.target.textContent === 'Delete') {
        let id = event.target.dataset.id;
        deleteStaffData(id)
    }
}

