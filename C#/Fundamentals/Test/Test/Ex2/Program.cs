using System;
using System.Collections.Generic;
using System.Linq;


namespace Ex2
{
    
    class Program
    {
        static void Main(string[] args)
        {
            int employeeCount = int.Parse(Console.ReadLine());
            List<Employee> employees = new List<Employee>();
            Dictionary<String, double> departmentSalary = new Dictionary<string, double>();
            
            for (int i = 0; i < employeeCount; i++)
            {
                string[] employeeData = Console.ReadLine().Split();
                string name = employeeData[0];
                double salary = double.Parse(employeeData[1]);
                string department = employeeData[2];
                if (!departmentSalary.ContainsKey(department))
                    departmentSalary[department] = 0;
                
                departmentSalary[department] += salary;
                
                Employee employee = new Employee(name, salary, department);
                employees.Add(employee);
            }

            Dictionary<String, double> sortedDepartment = departmentSalary.OrderByDescending(x => x.Value).ToDictionary(x => x.Key, x => x.Value);
            string biggestDepartment = sortedDepartment.First().Key;
            List<Employee> sortedEmployees = employees.OrderByDescending(x => x.Salary).ToList();
            
            Console.WriteLine($"Highest Average Salary: {biggestDepartment}");

            foreach (Employee employee in sortedEmployees)
                if (employee.Department == biggestDepartment)
                    Console.WriteLine($"{employee.Name} {employee.Salary:f2}");
        }
    }
}