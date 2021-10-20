using System;

namespace Ex1Dates
{
    class Program
    {
        static void Main(string[] args)
        {
            string firstDate = Console.ReadLine();
            string secondDate = Console.ReadLine();
            
            DateCounter dateCounter = new DateCounter(firstDate, secondDate);
            
            Console.WriteLine(dateCounter.CalculateDifference());
        }
    }
}