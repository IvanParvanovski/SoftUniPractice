// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex1NumbersSorter
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            List<long> numbers = new List<long>();
            int INPUT_ELEMENTS = 3;

            for (int i = 0; i < INPUT_ELEMENTS; i++) { numbers.Add(long.Parse(Console.ReadLine()!)); }
            
            while (numbers.Count > 0)
            {
                long biggestEl = numbers.Max();
                
                numbers.Remove(biggestEl);
                Console.WriteLine(biggestEl);
            } 
        }
    }
}