import { html, render } from '../node_modules/lit-html/lit-html.js';
import { students } from './students.js';

const tableTmp = (students, onSearch) => html`
    <table class="styled-table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Points</th>
            </tr>
        </thead>

        <tbody>
            ${students.map(s => studentTmp(s))}
        </tbody>
    </table>

    <div class="search">
        <input type="text" class="searchTerm">
        <button class="searchButton" @click=${(event) => onSearch(event)}>Search</button>
    </div>
`;

const studentTmp = (student) => html`
    <tr>
        <td class="{'active' or ''}">${student.name}</td>
        <td class="{'active' or ''}">${student.points}</td>
    </tr>
`

const root = document.querySelector('main');
page();

export function page() {
    render(tableTmp(students, onSearch), root);
}


function onSearch(event) {
    const searchSection = event.target.parentNode;

    const inputField = searchSection.querySelector('input.searchTerm');
    const searchedText = inputField.value.toLowerCase();
    
    const tableStudents = [...document.querySelectorAll('tr')];
    tableStudents.shift();

    if (searchedText == '') {
        return;
    }

    for (const ts of tableStudents) {
        const data = ts.querySelectorAll('td');
        const name = data[0].textContent;

        if (name.toLocaleLowerCase().includes(searchedText)) {
            data[0].className = 'active';
            data[1].className = 'active';
        } else {
            data[0].className = '';
            data[1].className = '';
        }
    }
}
