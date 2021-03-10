using System;
using System.Collections.Generic;

namespace Ex1COutCHarsInAString
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            Dictionary<char, int> lettersCount = new Dictionary<char, int>();
            foreach (char symbol in text)
            {
                if (symbol == ' ')
                    continue;

                if (!lettersCount.ContainsKey(symbol))
                    lettersCount[symbol] = 0;

                lettersCount[symbol] += 1;
            }

            foreach (var value in lettersCount)
                Console.WriteLine($"{value.Key} -> {value.Value}");
        }
    }
}
