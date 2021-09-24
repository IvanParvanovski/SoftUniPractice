using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex2OrderStudents
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] rawNumbers = Console.ReadLine().Split("|");
            List<int> result = new List<int>();
            
            foreach (var rawNum in rawNumbers.Reverse())
            {
                int[] numbers = rawNum
                    .Split(" ", StringSplitOptions.RemoveEmptyEntries)
                    .Select(int.Parse)
                    .ToArray();
                
                foreach (int num in numbers)
                {
                    result.Add(num);
                }
            }

            Console.WriteLine(string.Join(" ", result));
        }
    }
}