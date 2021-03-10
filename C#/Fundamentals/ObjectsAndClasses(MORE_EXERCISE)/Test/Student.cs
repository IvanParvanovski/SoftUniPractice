namespace Test
{
    public class Student : Person, 
                           IHuman 
    {
        public Student(int age) : base(age)
        {
            this.Age = age;
        }
        
        
        public string Walk(int steps)
        {
            return $"You walked {steps}!";
        }
    }
}
