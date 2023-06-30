using System;
using System.ComponentModel;

namespace Ex2
{
    public class SalesEmployee : IEmployee
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Department { get; set; }

        public decimal Salary { get; set; } = 1000;
        public decimal Profits { get; set; }

        public SalesEmployee(string firstName, string lastName, string department, decimal profits)
        {
            this.FirstName = firstName;
            this.LastName = lastName;
            this.Department = department;
            this.Profits = profits;
        }
        
        
        public decimal GetSalary()
        {
            return Profits * (decimal)0.1 + Salary;
        }

        public string ToString()
        {
            return $"{this.FirstName} {this.LastName} from {this.Department} has {this.Profits} profits.";
        }
    }
}