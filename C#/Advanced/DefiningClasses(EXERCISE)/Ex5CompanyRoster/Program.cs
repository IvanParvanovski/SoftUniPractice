using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex5CompanyRoster
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, List<Employee>> departments = new Dictionary<string, List<Employee>>();

            int employeesCount = int.Parse(Console.ReadLine()!);

            for (int i = 0; i < employeesCount; i++)
            {
                string[] employeeData = Console.ReadLine()!.Split();

                string name = employeeData[0];
                double salary = double.Parse(employeeData[1]);
                string position = employeeData[2];
                string department = employeeData[3];
                
                Employee employee = new Employee(
                    name,
                    salary,
                    position,
                    department
                );
                
                if (employeeData.Length == 5)
                {
                    int element;
                    if (int.TryParse(employeeData[4], out element))
                    {
                        employee.Age = element;
                    }
                    else
                    {
                        employee.Email = employeeData[4];
                    }
                } 
                else if (employeeData.Length == 6)
                {
                    string email = employeeData[4];
                    int age = int.Parse(employeeData[5]);
                    
                    employee.Email = email;
                    employee.Age = age;
                }

                if (!departments.ContainsKey(department))
                {
                    departments[department] = new List<Employee>();
                }
                
                departments[department].Add(employee);
            }

            Dictionary<string, List<Employee>> sortedDepartments = departments
                .OrderBy(x => x.Value
                    .Sum(e => e.Salary))
                    .ToDictionary(x => x.Key, x => x.Value);

            KeyValuePair<string, List<Employee>> firstDepartment = sortedDepartments.Last();
            Console.WriteLine($"Highest Average Salary: {firstDepartment.Key}");
            
            foreach (Employee employee in firstDepartment.Value.OrderByDescending(e => e.Salary))
            {
                Console.WriteLine(employee.ToString());
            }
        }
    }
}