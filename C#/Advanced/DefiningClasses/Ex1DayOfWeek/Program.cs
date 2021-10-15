using System;
using System.Globalization;

namespace Ex1DayOfWeek
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime inputData = DateTime.ParseExact(Console.ReadLine()!, "d-M-yyyy", CultureInfo.InvariantCulture);
            Console.WriteLine(inputData.DayOfWeek);
        }
    }
}