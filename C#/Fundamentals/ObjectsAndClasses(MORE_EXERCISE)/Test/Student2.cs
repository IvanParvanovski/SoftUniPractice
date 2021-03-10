namespace Test
{
    public class Student2 : IHuman
    {
        public string Grade(string element)
        {
            return element + "!";
        }

        public string Walk(int steps)
        {
            throw new System.NotImplementedException();
        }
    }
}