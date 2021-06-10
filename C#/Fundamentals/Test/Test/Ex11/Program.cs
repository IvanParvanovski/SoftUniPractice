using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex11
{
    
    class Program
    {
        static void Main(string[] args)
        {
            int employeesCount = int.Parse(Console.ReadLine());
            List<Employee> employees = new List<Employee>();
            
            for (int i = 0; i < employeesCount; i++)
            {
                string[] data = Console.ReadLine().Split();
                employees.Add(new Employee(data[0], data[1], double.Parse(data[2])));
            }

            foreach (Employee employee in employees.OrderBy(x => x.Salary).Reverse())
            {
                Console.WriteLine(employee);
            }

        }
    }
}