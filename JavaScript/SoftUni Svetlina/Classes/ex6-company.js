class Company {
    constructor() {
        this.departments = {};
    }

    isEmpty(val) {
        return val == '' || val == undefined || val == null; 
    }

    // New employee is hired. Name: Stanimir. Position. engineer
    // New employee is hired. Name: Stanimir. Position: engineer

    addEmployee(username, salary, position, department) {
        if (this.isEmpty(username) || 
            this.isEmpty(salary) ||
            this.isEmpty(position) ||
            this.isEmpty(department) ) {
                throw new Error('Invalid input!');
            }
        else if (salary < 0) {
            throw new Error('Invalid input!');
        }

        if (!(department in this.departments)) {
            this.departments[department] = [];
        } 

        this.departments[department].push( {username, salary, position} );
        return `New employee is hired. Name: ${username}. Position: ${position}`;
    }

    bestDepartment() {
        let bd = '';
        let bdAverage = 0;

        for (const department of Object.entries(this.departments)) {
            const average = department[1].reduce((prevVal, nextVal) => prevVal + nextVal.salary, 0) / department[1].length;
            
            if (average > bdAverage) {
                bdAverage = average;
                bd = department[0];
            }
        }

        return `Best Department is: ${bd}\nAverage salary: ${bdAverage.toFixed(2)}\n` + 
                Object
                    .values(this.departments[bd])
                    .sort((a, b) => {
                        let res = a.salary - b.salary

                        if (res > 0) {
                            return -1;
                        } else if (res < 0) {
                            return 1;
                        }

                        return a.username.localeCompare(b.username);
                    })
                    .map(x => `${x.username} ${x.salary} ${x.position}`
                ).join('\n');
        };
}

let c = new Company();
c.addEmployee("Stanimir", 2000, "engineer", "Construction");
c.addEmployee("Pesho", 1500, "electrical engineer", "Construction");
c.addEmployee("Slavi", 500, "dyer", "Construction");
c.addEmployee("Stan", 2000, "architect", "Construction");
c.addEmployee("Stanimir", 1200, "digital marketing manager", "Marketing");
c.addEmployee("Pesho", 1000, "graphical designer", "Marketing");
c.addEmployee("Gosho", 1350, "HR", "Human resources");
console.log(c.bestDepartment());
