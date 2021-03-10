namespace Ex4Students
{
    public class Student
    {
        public string FistName { get; set; }
        public string LastName { get; set; }
        public double Grade { get; set; }

        public Student(string firstName, string lastName, double grade)
        {
            this.FistName = firstName;
            this.LastName = lastName;
            this.Grade = grade;
        }

        public override string ToString()
        {
            return $"{FistName} {LastName}: {Grade:f2}";
        }
    }
}