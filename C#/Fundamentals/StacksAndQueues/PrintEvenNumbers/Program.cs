using System;
using System.Collections.Generic;
using System.Linq;

namespace PrintEvenNumbers
{
    class Program
    {
        static void Main(string[] args)
        {
            Queue<int> numbers = new Queue<int>(Console.ReadLine()!
                                                       .Split()
                                                       .Select(int.Parse));
            
            List<int> result = new List<int>();
            
            while (numbers.Count > 0)
            {
                int num = numbers.Dequeue();

                if (num % 2 == 0)
                    result.Add(num);
            }
            
            Console.WriteLine(string.Join(", ", result));
        }
    }
}
