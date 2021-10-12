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

      document.getElementById('bestRestaurant').textContent = bestRestaurant[0];
      // document.getElementById('workers') = Object.keys(bestRestaurant[1]).join(' ');
   }
}
