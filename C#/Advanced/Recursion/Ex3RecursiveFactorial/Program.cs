using System;

namespace Ex3RecursiveFactorial
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            Console.WriteLine(Factorial(n, 1));
        }

        private static int Factorial(int n, int sum)
        {
            if (n == 1)
            {
                return sum;
            }

            sum *= n;
            return Factorial(n - 1, sum);
        }
    }
}