using System;
using System.Linq;

namespace Ex3RoundingNumbers
{
    class Program
    {
        static void Main(string[] args)
        {
            double[] numbers = Console.ReadLine().Split(" ")
                               .Select(double.Parse)
                               .ToArray();

            foreach (decimal num in numbers)
                Console.WriteLine($"{num} => {Math.Round(num, MidpointRounding.AwayFromZero)}");
        }
    }
}
