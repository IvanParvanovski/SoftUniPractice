using System.ComponentModel;

namespace Ex2
{
    public class Junior: IEmployee
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Department { get; set; }

        public decimal Salary { get; set; } = 900;

        public Junior(string firstName, string lastName, string department)
        {
            this.FirstName = firstName;
            this.LastName = lastName;
            this.Department = department;
        }
        
        public decimal GetSalary()
        {
            return Salary;
        }

        public string ToString()
        {
            return $"{FirstName} {LastName} is {Department} engineer.";
        }
    }
}