// See https://aka.ms/new-console-template for more information

using System;
using System.Linq;

namespace Ex2Searching
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int[] numbers = Console.ReadLine()!.Split().Select(int.Parse).ToArray();
            int searchedNum = int.Parse(Console.ReadLine()!);

            Console.WriteLine(LinearSearch(numbers, searchedNum));
        }

        public static int LinearSearch(int[] arr, int number)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] == number)
                {
                    return i;
                }
            }
            
            return -1;
        }
    }
}