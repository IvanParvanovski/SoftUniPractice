using System;
using System.Linq;

namespace Ex5SumEvenNumbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] numbers = Console.ReadLine()
                            .Split(" ")
                            .Select(x => IsNumEven(int.Parse(x)))
                            .ToArray();

            Console.WriteLine(numbers.Sum());
        }

        private static int IsNumEven(int num)
        {
            return num % 2 == 0 ? num : 0;
        }
    }
}
