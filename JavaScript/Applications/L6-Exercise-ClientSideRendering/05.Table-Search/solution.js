import { html, render } from './node_modules/lit-html/lit-html.js';

const rowTmp = (student) => html`
<tr class="${student.status ? 'select' : ''}">
   <td>${student.firstName} ${student.lastName}</td>
   <td>${student.email}</td>
   <td>${student.course}</td>
</tr>`;


const students = Object.values(await loadStudents());
const tableBody = document.querySelector('tbody'); 
document.querySelector('#searchBtn').addEventListener('click', onClick);

update();

async function onClick() {
   const searchedTextField = document.getElementById('searchField')
   const searchedText = searchedTextField.value.trim().toLowerCase();

   for (const student of students) {
      const studentData = Object.values(student);
      studentData.pop();

      student.status = studentData.some(
         x => searchedText && x.toLowerCase().includes(searchedText)
      );
   }

   searchedTextField.value = '';
   update();
}

function update() {
   render(students.map(rowTmp), tableBody);
}

function loadStudents() {
   return request('http://localhost:3030/jsonstore/advanced/table');
}

async function request(url, options) {
   try {
      const response = await fetch(url, options);

      if (response.ok == false) {
         const message = response.json();
         throw new Error(message);
      }

      const data = await response.json();
      return data;
   } catch (err) {
      alert(err);
   }
}
