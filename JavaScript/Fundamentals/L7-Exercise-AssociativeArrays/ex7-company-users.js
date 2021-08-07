function companies(input) {
    
    let companiesWorkers = {};

    // Iterate threw each hired employee data
    // Check if the given company exists, if not add it and
    // add the given employee, otherwise just add the employee

    for (let hiredInfo of input) {
        let [company, employeeId] = hiredInfo.split(' -> ');

        if (!(company in companiesWorkers)) {
            companiesWorkers[company] = [];
        }

        let companyEmployees = companiesWorkers[company];

        if (!companyEmployees.includes(employeeId)) {
            companyEmployees.push(employeeId);
        }
    }

    // Sort the companies alphabetically
    let sortedCompanies = Object.entries(companiesWorkers).sort((a, b) => a[0].localeCompare(b[0]));

    // Display the companies and their employees
    for (let [company, employees] of sortedCompanies) {
        console.log(company);

        employees.forEach(employee => {
            console.log('-- ' + employee);
        });
    }
}

companies([
    'SoftUni -> AA12345',
    'SoftUni -> BB12345',
    'Microsoft -> CC12345',
    'HP -> BB12345'
]);