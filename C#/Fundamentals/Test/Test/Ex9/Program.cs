using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex9
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            Dictionary<char, int> result = new Dictionary<char, int>();
            foreach (char symbol in text)
            {
                if (!result.ContainsKey(symbol))
                    result[symbol] = 0;
                result[symbol] += 1;
            }

            foreach (var r in result.OrderBy(x => x.Key))
                Console.WriteLine($"{r.Key}: {r.Value} time/s");
            
        }
    }
}
