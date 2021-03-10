using System;

namespace Ex1
{
    public class Employee
    {
        public String FirstName { get; set; }
        public String LastName { get; set; }
        public double Salary { get; set; }

        public Employee(string firstName, string lastName, double salary)
        {
            this.FirstName = firstName;
            this.LastName = lastName;
            this.Salary = salary;
        }

        public override string ToString()
        {
            return $"{FirstName} {LastName}: {Salary:f2}";
        }
    }
}