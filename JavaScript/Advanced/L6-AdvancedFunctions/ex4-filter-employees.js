function company(employees, standard) {
    const [data, criteria] = standard.split('-');
    const validEmployees = JSON.parse(employees).filter((e) => e[data] == criteria);
    validEmployees.forEach((employee, index) => {
        const employeeFullName = `${employee.first_name} ${employee.last_name}`;
        console.log(`${index}. ${employeeFullName} - ${employee.email}`);
    });
}

company(`[{
    "id": "1",
    "first_name": "Ardine",
    "last_name": "Bassam",
    "email": "abassam0@cnn.com",
    "gender": "Female"
  }, {
    "id": "2",
    "first_name": "Kizzee",
    "last_name": "Jost",
    "email": "kjost1@forbes.com",
    "gender": "Female"
  },  
{
    "id": "3",
    "first_name": "Evanne",
    "last_name": "Maldin",
    "email": "emaldin2@hostgator.com",
    "gender": "Male"
  }]`, 
'gender-Female'
);
