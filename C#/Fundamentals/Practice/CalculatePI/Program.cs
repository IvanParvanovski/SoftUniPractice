using System;

namespace CalculatePI
{
    class Program
    {
        public static double MonteCarloPI(int n)
        {
            Random rand = new Random();
            int pointsIn = 0;
            for (int i = 0; i < n; i++)
            {
                double x = rand.NextDouble();
                double y = rand.NextDouble();
                if (Math.Sqrt(x * x + y * y) <= 1)
                {
                    pointsIn++;
                }
            }
            return 4.0 * (double)pointsIn / n;
        }
        static void Main(string[] args)
        {
            Console.WriteLine("PI = " + MonteCarloPI(10));
            Console.WriteLine("PI = " + MonteCarloPI(100));
            Console.WriteLine("PI = " + MonteCarloPI(10000));
            Console.WriteLine("PI = " + MonteCarloPI(1000000));
            Console.WriteLine("PI = " + MonteCarloPI(100000000));
        }
    }
}