using System;
using System.Linq;

namespace Ex6EvenAndOddSubtraction
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] numbers = Console.ReadLine().Split(" ")
                            .Select(int.Parse)
                            .ToArray();

            int[] evenNumbers = FilterNumbers(numbers, IsEven);
            int[] oddNumbers = FilterNumbers(numbers, IsOdd);

            int evenSum = evenNumbers.Sum();
            int oddSum = oddNumbers.Sum();
            int result = evenSum - oddSum;

            Console.WriteLine(result);
        }

        private static bool IsEven(int num)
        {
            return num % 2 == 0;
        }

        private static bool IsOdd(int num)
        {
            return num % 2 != 0;
        }

        private static int[] FilterNumbers(int[] numbers, Func<int, bool> check)
        {
            return (from num in numbers where check(num) select num).ToArray();
            //return numbers.Where(x => check(x)).ToArray();
        }
    }
}
