import { html, render } from './node_modules/lit-html/lit-html.js';

const optionsTmp = (option) => html`<option value="${option._id}">${option.text}</option>`;

const menu = document.getElementById('menu');

const form = document.querySelector('form');
form.addEventListener('submit', addItem);

update();

async function addItem(event) {
    event.preventDefault();

    const formData = new FormData(form);
    const text = formData.get('itemText');

    await addOption({ text });
    update();
    form.reset();
}

async function loadOptions() {
    return request('http://localhost:3030/jsonstore/advanced/dropdown');
}

async function addOption(data) {
    return request('http://localhost:3030/jsonstore/advanced/dropdown', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    });
}

async function update() {
    const options = Object.values(await loadOptions());
    render(options.map(optionsTmp), menu);
}

async function request(url, options) {
    try {
        const response = await fetch(url, options);

        if (response.ok == false) {
            throw new Error(`${response.status} ${response.text}`);
        }
    
        const data = await response.json();
        return data;
    } catch (err) {
        alert(err);
    }
}
