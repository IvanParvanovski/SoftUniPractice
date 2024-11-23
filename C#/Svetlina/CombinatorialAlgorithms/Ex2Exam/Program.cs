namespace Ex2Exam
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var v1 = int.Parse(Console.ReadLine());
            var v2 = int.Parse(Console.ReadLine());
            var v3 = int.Parse(Console.ReadLine());

            Console.WriteLine(Calculate(v1, v2, v3));
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