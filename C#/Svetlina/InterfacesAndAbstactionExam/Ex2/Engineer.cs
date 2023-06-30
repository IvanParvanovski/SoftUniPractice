using System.ComponentModel;

namespace Ex2
{
    public class Engineer: IEmployee
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Department { get; set; }

        public decimal Salary { get; set; } = 1300;
        public int YearsService { get; set; }

        public Engineer(string firstName, string lastName, string department, int years)
        {
            this.FirstName = firstName;
            this.LastName = lastName;
            this.Department = department;
            this.YearsService = years;
        }
        
        
        public decimal GetSalary()
        {
            return this.Salary + YearsService * 90;
        }

        public string ToString()
        {
            return $"{FirstName} {LastName} from {Department} has {YearsService} years of service.";
        }
    }
}