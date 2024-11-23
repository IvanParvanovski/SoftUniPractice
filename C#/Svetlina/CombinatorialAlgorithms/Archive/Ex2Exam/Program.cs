namespace Ex2Exam
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine(Calculate(10, 2, 16));
            Console.WriteLine(Calculate(10, 30, 20));
        }

        public static string Calculate(int days, int requiredCups, int maxCups)
        {
            int needed = days * requiredCups;
            int wanted = days * maxCups;

            if (needed > wanted)
            {
                return "No, you won't have enough coffee till your next paycheck";
            }


            return "Yes, you will have enough coffee till your next paycheck";
        }
    }
}