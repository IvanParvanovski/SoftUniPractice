namespace Ex5CompanyRoster
{
    public class Employee
    {
        private string _name;
        private double _salary;
        private string _position;
        private string _department;
        private string _email;
        private int _age;

        public Employee(
            string name,
            double salary,
            string position,
            string department,
            string email = "n/a",
            int age = -1)
        {
            this.Name = name;
            this.Salary = salary;
            this.Position = position;
            this.Department = department;
            this.Email = email;
            this.Age = age;
        }

        public string Name
        {
            get => _name;
            set => _name = value;
        }

        public double Salary
        {
            get => _salary;
            set => _salary = value;
        }

        public string Position
        {
            get => _position;
            set => _position = value;
        }

        public string Department
        {
            get => _department;
            set => _department = value;
        }

        public string Email
        {
            get => _email;
            set => _email = value;
        }

        public int Age
        {
            get => _age;
            set => _age = value;
        }

        public override string ToString()
        {
            return $"{_name} {_salary:f2} {_email} {_age}";
        }
    }
}