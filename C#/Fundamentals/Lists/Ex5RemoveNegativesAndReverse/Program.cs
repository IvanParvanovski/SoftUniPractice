using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex5RemoveNegativesAndReverse
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = Console.ReadLine().Split().Select(int.Parse).ToList();
            numbers = numbers.Where(x => x >= 0).ToList();
            if (numbers.Count == 0)
            {
                Console.WriteLine("empty");
                return;
            }
            numbers.Reverse();
            
            Console.WriteLine(string.Join(" ", numbers));
        }
    }
}
