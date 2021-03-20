using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex22
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            string result = new string(text!.OrderBy(x => x).ToArray());
            Dictionary<char, int> resultDict = new Dictionary<char, int>();
            foreach (char symbol in result)
            {
                if (!resultDict.ContainsKey(symbol))
                    resultDict[symbol] = 0;
                resultDict[symbol]++;
            }

            Console.WriteLine(result);
            foreach (var pair in resultDict)
                Console.WriteLine($"{pair.Key} -> {pair.Value}");
            
        }
    }
}