const form = document.getElementById('form');
const tableBody = document.querySelector('#results tbody');

form.addEventListener('submit', addStudent);
displayStudents();

async function displayStudents(event) {
    const students = await getStudents();

    for (const student of Object.values(students)) {
        tableBody.appendChild(createTableData(student));
    }
}

function createTableData(data) {
    const tableRow = document.createElement('tr');
    const values = Object.entries(data);
    values.pop();

    for (const token of values) {
        const tableData = document.createElement('td');
        tableData.textContent = token[1];

        tableRow.appendChild(tableData);
    }

    return tableRow;
}

function addStudent(event) {
    const formData = new FormData(form);
    const studentInfo = {
        firstName: formData.get('firstName').trim(),
        lastName: formData.get('lastName').trim(),
        facultyNumber: formData.get('facultyNumber').trim(),
        grade: Number(formData.get('grade').trim()),
    }

    try {
        if (Object.values(studentInfo).some(x => x == undefined)) {
            throw new Error('All fields should be filled!');
        }
    
        createTableData(studentInfo);
        createStudent(studentInfo);
        form.reset();
    } catch (err) {
        alert(err);
    }

}

async function createStudent(studentInfo) {
    const url = 'http://localhost:3030/jsonstore/collections/students';
    const record = {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(studentInfo)        
    };

    const response = await fetch(url, record);

    if (response.status != 200) {
        throw new Error(`${response.status} ${response.statusText}`);
    }

    return await response.json();
}

async function getStudents() {
    const url = 'http://localhost:3030/jsonstore/collections/students';
    const response = await fetch(url);

    if (response.status != 200) {
        throw new Error(`${response.status} ${response.statusText}`);
    }

    return response.json();
}
