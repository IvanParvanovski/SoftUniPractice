function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function sum(numbers) {
      return numbers.reduce((total, currentValue) => {
         total += currentValue;
         return total;
      }, 0);
   }

   function average(numbers) {
      return numbers.length / sum(numbers);
   }

   function onClick() {
      const input = document.querySelector('#inputs textarea').value;
      const restaurants = {};

      const regexPattern = /(?<restaurantName>\w+) - (?<employees>(\w+ \d+, )+(\w+ \d+))/g;
      const regex = new RegExp(regexPattern);

      while (true) {
         const match = regex.exec(input);
         
         if (match == null) {
            break;
         }

         const restaurantName = match.groups.restaurantName;
         const employees = match.groups.employees.split(', ');

         if (!(restaurantName in restaurants)) {
            restaurants[restaurantName] = {};
         }

         const restaurant = restaurants[restaurantName];

         for (const employee of employees) {
            const [employeeName, employeeSalary] = employee.split(' ');
            restaurant[employeeName] = Number(employeeSalary);
         }
      }
      
      const sortedRestaurantByAverageSalary = Object.entries(restaurants).sort((a, b) => average(Object.values(a[1])) - average(Object.values(b[1])));
      const bestRestaurant = sortedRestaurantByAverageSalary[0];

      const sortedEmployees = Object.entries(bestRestaurant[1]).sort((a, b) => b[1] - a[1]);
      
      let averageSalary = 0;
      let bestSalary = Number.MIN_SAFE_INTEGER;
      let workers = [];

      for (let [employee, salary] of sortedEmployees) {
         averageSalary += salary;
         
         if (salary > bestSalary) {
            bestSalary = salary;
         }

         workers.push(`Name ${employee} With Salary: ${salary}`);
      }
      
      averageSalary /= sortedEmployees.length;

      document.querySelector('#bestRestaurant p').textContent = (
       `Name: ${bestRestaurant[0]} ` +
       `Average Salary: ${averageSalary.toFixed(2)} ` +
       `Best Salary: ${bestSalary.toFixed(2)}`
      );

      document.querySelector('#workers p').textContent = workers.join(' ');
   }
}
