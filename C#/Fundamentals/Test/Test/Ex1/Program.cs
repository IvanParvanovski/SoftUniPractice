using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex1
{
    
    class Program
    {
        static void Main(string[] args)
        {
            int employeesCount = int.Parse(Console.ReadLine());
            List<Employee> employees = new List<Employee>();
            
            for (int i = 0; i < employeesCount; i++)
            {
                string[] employeeData = Console.ReadLine().Split();
                string firstName = employeeData[0];
                string lastName = employeeData[1];
                double salary = double.Parse(employeeData[2]);

                Employee employee = new Employee(firstName, lastName, salary);
                employees.Add(employee);
            }

            List<Employee> orderedEmployees = employees.OrderByDescending(x => x.Salary).ToList();
            foreach (Employee employee in orderedEmployees)
                Console.WriteLine(employee);
        }
    }
}