using System;
using System.Collections.Generic;
using System.Text;

namespace Ex5DigitsLettersOthers
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();

            Dictionary<string, StringBuilder> result = new Dictionary<string, StringBuilder>()
            {
                {"digits", new StringBuilder()},
                {"letter", new StringBuilder()},
                {"symbols", new StringBuilder()}
            };

            if (input != null)
                foreach (char symbol in input)
                {
                    if (Char.IsLetter(symbol))
                        result["letter"].Append(symbol);
                    else if (Char.IsDigit(symbol))
                        result["digits"].Append(symbol);
                    else
                        result["symbols"].Append(symbol);
                }

            foreach (StringBuilder output in result.Values)
                Console.WriteLine(output.ToString());
        }
    }
}