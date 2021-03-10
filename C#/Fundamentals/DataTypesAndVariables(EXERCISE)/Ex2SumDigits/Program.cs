using System;

namespace Ex2SumDigits
{
    class Program
    {
        static void Main(string[] args)
        {
            int num = Int32.Parse(Console.ReadLine());
            Console.WriteLine(CalculateSumOfDigits(num));
        }
        private static int CalculateSumOfDigits(int num)
        {
            int sumOfDigits = 0;
            int operationalNumber = num;
            
            while (operationalNumber > 0)
            {
                sumOfDigits += operationalNumber % 10;
                operationalNumber /= 10;
            }

            return sumOfDigits;
        }
    }
}
