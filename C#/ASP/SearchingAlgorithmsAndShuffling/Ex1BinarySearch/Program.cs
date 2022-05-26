using System;
using System.Linq;

namespace Ex1BinarySearch
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int[] numbers = Console.ReadLine()!
                .Split(" ")
                .Select(int.Parse)
                .ToArray();

            int element = int.Parse(Console.ReadLine()!);

            Console.WriteLine(IndexOf(numbers, element));
        }

        public static int IndexOf(int[] arr, int key)
        {
            int leftIndex = 0;
            int rightIndex = arr.Length - 1;

            while (leftIndex <= rightIndex)
            {
                int midIndex = leftIndex + (rightIndex - leftIndex) / 2;

                if (key < arr[midIndex])
                {
                    rightIndex = midIndex - 1;
                }
                else if (key > arr[midIndex])
                {
                    leftIndex = midIndex + 1;
                }
                else
                {
                    return midIndex;
                }
            }

            return -1;
        }
    }
}