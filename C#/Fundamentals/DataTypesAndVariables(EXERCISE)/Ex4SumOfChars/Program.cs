using System;

namespace Ex4SumOfChars
{
    class Program
    {
        static void Main(string[] args)
        {
            int symbolsCount = Int32.Parse(Console.ReadLine());
            Console.WriteLine($"The sum equals: {CalculateCharSum(symbolsCount)}");
        }

        private static int CalculateCharSum(int symbolsCount)
        {
            int sum = 0;
            for (int i = 0; i < symbolsCount; i++)
                sum += Convert.ToInt32(char.Parse(Console.ReadLine()));
            return sum;
        }
    }
}
