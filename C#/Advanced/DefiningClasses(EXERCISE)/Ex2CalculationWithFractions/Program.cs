using System;
using System.Linq;
using Fractions;

namespace Ex2CalculationWithFractions
{
    class Program
    {
        static void Main(string[] args)
        {
            string userInput = Console.ReadLine()!;
            string[] data = userInput!.Split(" ", StringSplitOptions.RemoveEmptyEntries);

            long[] firstFraction = data[0].Split('/').Select(long.Parse).ToArray();
            long[] secondFraction = data[2].Split('/').Select(long.Parse).ToArray();
            string operation = data[1];
           
            Fraction f1 = new Fraction(firstFraction[0], firstFraction[1]);
            Fraction f2 = new Fraction(secondFraction[0], secondFraction[1]);

            Console.WriteLine($"{userInput} = {new CalculateFractions(f1, f2, operation).Calculate()}");
        }
    }
}