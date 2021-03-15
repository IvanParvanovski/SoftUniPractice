using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex23
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = Console.ReadLine().Split();
            string[] orderedWords = words.OrderBy(x => x).ToArray();
            Dictionary<string, int> result = new Dictionary<string, int>();
            
            foreach (string word in orderedWords)
            {
                if (!result.ContainsKey(word))
                    result[word] = 0;
                result[word]++;
            }

            Console.WriteLine(string.Join(" ", orderedWords));
            foreach (var pair in result)
                Console.WriteLine($"{pair.Key} -> {pair.Value}");
        }
    }
}