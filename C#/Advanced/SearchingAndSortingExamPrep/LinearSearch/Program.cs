// See https://aka.ms/new-console-template for more information

using System;

namespace LinearSearch
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int[] numbers = {1, 3, 4, 10, 8};
            int searchedNumber = 4;
            
            for (int i = 0; i < numbers.Length; i++)
            {
                if (numbers[i] == searchedNumber)
                {
                    Console.WriteLine(i);
                    break;
                }
            }            
        }
    }
}