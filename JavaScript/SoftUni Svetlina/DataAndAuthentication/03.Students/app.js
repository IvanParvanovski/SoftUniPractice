async function solve() {
    const students = await (await fetch('http://localhost:3030/jsonstore/collections/students')).json();
    const table = document.querySelector('#results tbody');

    const firstName = document.querySelector('input[name="firstName"]');
    const lastName = document.querySelector('input[name="lastName"]');
    const facultyNumber = document.querySelector('input[name="facultyNumber"]');
    const grade = document.querySelector('input[name="grade"]');

    document.getElementById('submit').addEventListener('click', onSubmit);
    
    for (const studentId in students) {
        const tr = document.createElement('tr');
        const student = students[studentId];
        console.log(student);
        
        tr.innerHTML = [
            `<th>${student.firstName}</th>`,
            `<th>${student.lastName}</th>`,
            `<th>${student.facultyNumber}</th>`,
            `<th>${student.grade}</th>`,
        ].join('');

        table.appendChild(tr);
    }

    async function onSubmit() {
        const response = await fetch('http://localhost:3030/jsonstore/collections/students', {
            method: 'post',
            headers: {'Content-Type': 'application/json', },
            body: JSON.stringify({
                firstName: firstName.value, 
                lastName: lastName.value, 
                facultyNumber: facultyNumber.value,
                grade: grade.value
            })
        });

        console.log(response);
    }
}

solve();