using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex22
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // ccc-aaa-bbb
            
            // Output:
            // ---aaabbbccc
            // - -> 2
            // a -> 3
            // b -> 3
            // c -> 3

            // Read user's input
            string text = Console.ReadLine();
            string result = new string(text!.OrderBy(x => x).ToArray());
            
            // Initialize a hash table to keep the count of the letters in the text
            Dictionary<char, int> resultDict = new Dictionary<char, int>();
            
            // Add or increase each symbol count in the dictionary 
            foreach (char symbol in result)
            {
                if (!resultDict.ContainsKey(symbol))
                    resultDict[symbol] = 0;
                resultDict[symbol]++;
            }

            // Print the result
            Console.WriteLine(result);
            foreach (var pair in resultDict)
                Console.WriteLine($"{pair.Key} -> {pair.Value}");
            
        }
    }
}