using System;
using System.Text;

namespace Ex24
{
    class Program
    {
        static void Main(string[] args)
        {
            string word = Console.ReadLine();
            StringBuilder result = new StringBuilder();
            char previousSymbol = ' ';
            foreach (char symbol in word)
            {
                if (result.Length == 0)
                {
                    result.Append(symbol);
                    previousSymbol = symbol;
                    continue;
                }
                
                if (symbol != previousSymbol)
                    result.Append(symbol);
                previousSymbol = symbol;
            }

            Console.WriteLine(result);
        }
    }
}