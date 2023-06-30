// See https://aka.ms/new-console-template for more information

using System;
using System.Linq;

namespace Ex2
{
    public class Program
    {
        public delegate void CustomAggregate(int[] numbers);
        
        public static void Main(string[] args)
        {
            var customAggregate = new CustomAggregate(DisplayLength);
            
            customAggregate += DisplaySum;
            
            int[] numbers = Console.ReadLine()
                .Split(", ")
                .Select(int.Parse)
                .ToArray();

            customAggregate.Invoke(numbers);
        }

        private static void DisplayLength(int[] numbers)
        {
            Console.WriteLine(numbers.Length);
        }

        private static void DisplaySum(int[] numbers)
        {
            Console.WriteLine(numbers.Aggregate((sum, val) => sum + val));
        }
    }
}