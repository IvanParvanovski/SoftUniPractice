using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex2ReadAndCount
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            Dictionary<char, int> symbolsCount = new Dictionary<char, int>();
            
            foreach (char symbol in text)
            {
                if (!symbolsCount.ContainsKey(symbol))
                {
                    symbolsCount[symbol] = 0;
                }
                symbolsCount[symbol]++;
            }
            
            foreach (KeyValuePair<char, int> item in symbolsCount.OrderBy(x => x.Key))
            {
                Console.WriteLine($"{item.Key}: {item.Value} time/s");
            }
        }
    }
}