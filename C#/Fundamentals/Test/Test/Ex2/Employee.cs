using System;

namespace Ex2
{
    public class Employee
    {
        public String Name { get; set; }
        public double Salary { get; set; }
        public String Department { get; set; }

        public Employee(string name, double salary, string department)
        {
            this.Name = name;
            this.Salary = salary;
            this.Department = department;
        }
    }
}