// See https://aka.ms/new-console-template for more information

using System;

namespace BinarySearch
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            // Should be ordered
            
            Console.WriteLine(BinarySearch(
                new[] {1, 2, 3, 4, 5, 6}, 
                6)
            );
        }

        public static int BinarySearch(int[] numbers, int searchNumber)
        {
            var left = 0;
            var right = numbers.Length - 1;

            while (left <= right)
            {
                var mid = (left + right) / 2;

                if (searchNumber == numbers[mid])
                {
                    return mid;
                }
                
                if (searchNumber > numbers[mid])
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid - 1;
                }
            }

            return -1;
        }
    }
}