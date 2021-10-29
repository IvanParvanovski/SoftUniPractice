using System;
using System.Linq;

namespace Ex1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] date1Tokens = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int[] date2Tokens = Console.ReadLine().Split().Select(int.Parse).ToArray();
            
            DateTime newDate1 = new DateTime(date1Tokens[0], date1Tokens[1], date1Tokens[2]);
            DateTime newDate2 = new DateTime(date2Tokens[0], date2Tokens[1], date2Tokens[2]);

            DateDifferenceCalculator cal = new DateDifferenceCalculator();
            Console.WriteLine(Math.Abs(cal.daysDifference(newDate1, newDate2)));
        }
    }
}