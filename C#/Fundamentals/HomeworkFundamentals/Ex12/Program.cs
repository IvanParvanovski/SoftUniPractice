using System;
using System.Globalization;

namespace Ex12
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // 550
            // 0.005
            // 1
            
            // Output:
            
            //          550.00
            //            100%
            //            0226
            //         $550.00
            //      5.5 * 10^2
            
            //           0.01
            //             0%
            //           0000
            //          $0.01
            //      5 * 10^-3
            
            //           1.00
            //             1%
            //           0001
            //          $1.00
            //       1 * 10^0

            // Read number
            double inputNumber = double.Parse(Console.ReadLine()!);
            
            // Get the result of the methods
            string floatingPoint = FloatingPoint(inputNumber);
            string percentage = Percentage(inputNumber);
            string hexadecimal = Hexadecimal(inputNumber);
            string currency = Currency(inputNumber);
            string scientificNotation = ScientificNotation(inputNumber);
            
            // Print the result
            Console.WriteLine(new string(' ', LengthDiff(floatingPoint)) + floatingPoint);
            Console.WriteLine(new string(' ', LengthDiff(percentage)) + percentage);
            Console.WriteLine(new string(' ', LengthDiff(hexadecimal)) + hexadecimal);
            Console.WriteLine(new string(' ', LengthDiff(currency)) + currency);
            Console.WriteLine(new string(' ', LengthDiff(scientificNotation)) + scientificNotation);
        }
        
        private static int LengthDiff(string text)
        {
            // Calculates the difference between the max length and the current string 
            return 15 - text.Length;
        }

        private static string FloatingPoint(double number)
        {
            // Returns the number with floating point
            return $"{number:f2}";
        }

        private static string Percentage(double number)
        {
            // Returns 100% if the number is more than or equal to 100
            // In other circumstances returns the number + '%'
            int numberInt = (int)number;
            if (numberInt >= 100)
                return "100%";
            return numberInt + "%";
        }

        private static string Hexadecimal(double number)
        {
            // Returns the number as hexadecimal
            return $"{(int)number:X4}";
        }

        private static string Currency(double number)
        { 
            // Returns the number as a currency
            return $"{number:C}";
        }

        private static string ScientificNotation(double number)
        {
            // Returns the number represented as scientific notation

            double[] scientificResult;
            if (number >= 1) 
                scientificResult = NotationPowerIntNumber(number, 0);
            else
                scientificResult = NotationPowerRealNumber(number, 0);

            string resultNumber = scientificResult[0].ToString(CultureInfo.InvariantCulture);
            string resultPower = scientificResult[1].ToString(CultureInfo.InvariantCulture);

            return $"{resultNumber} * 10^{resultPower}";
        }

        private static double[] NotationPowerIntNumber(double number, int counter)
        {
            // Calculates the power of a positive number
            if (number < 10)
                return new double[2] {number, counter};
            
            return NotationPowerIntNumber(number / 10, ++counter);
        }
        
        private static double[] NotationPowerRealNumber(double number, int counter)
        {
            // Calculates the power of a negative number
            if (number > 1)
                return new double[2] {number, counter};
            
            return NotationPowerRealNumber(number * 10, --counter);
        }
    }
}