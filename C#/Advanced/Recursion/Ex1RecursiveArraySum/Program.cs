using System;
using System.Linq;

namespace Ex1RecursiveArraySum
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int[] numbers = Console.ReadLine()?
                .Split()
                .Select(int.Parse)
                .ToArray();
            
            Console.WriteLine(Sum(numbers, 0));
        }

        private static int Sum(int[] array, int index, int sum=0)
        {
            if (array.Length == index)
            {
                return sum;
            }

            sum += array[index];
            return Sum(array, index + 1, sum);
        }
    }
}