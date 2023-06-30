namespace Ex1
{
    public class Employee: IPerson
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Department { get; set; }
        public int EmployeeId { get; set; }

        public Employee(string firstName, string lastName, string department, int employeeId)
        {
            this.FirstName = firstName;
            this.LastName = lastName;
            this.Department = department;
            this.EmployeeId = employeeId;
        }
        public string StartWorkingDay()
        {
            return
                $"{this.FirstName} {this.LastName} with id {this.EmployeeId} starts a new working day in the department {this.Department}.";
        }
    }
}