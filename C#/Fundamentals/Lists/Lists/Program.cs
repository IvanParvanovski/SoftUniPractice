using System;
using System.Collections.Generic;
using System.Linq;

namespace Lists
{
    class Program
    {
        static void Main(string[] args)
        {
            List<double> numbers = Console.ReadLine().Split().Select(double.Parse).ToList();
            int count = numbers.Count / 2;
            for (int i = 0; i < count; i++)
            {
                int n = numbers.Count - 1;
                numbers[i] += numbers[n];
                numbers.RemoveAt(n);
            }
            Console.WriteLine(string.Join(" ", numbers));
        }
    }
}
