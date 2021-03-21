using System;
using System.Diagnostics;
using System.Text;

namespace Ex24
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // IIvvaann
            // aaaaaaabbbbbbbbbbbcccccccdddddddfffffff
            
            // Output:
            // Ivan
            // abcdf
            
            // Read user's input and check if it is not null
            string word = Console.ReadLine();
            Debug.Assert(word != null, nameof(word) + " != null");

            // Initialize a string builder object to keep the result
            StringBuilder result = new StringBuilder();
            
            // Add the first symbol of the word
            result.Append(word[0]);
            char previousSymbol = word[0];
            
            // Add other symbols except the first one
            for (int i = 1; i < word.Length; i++)
            {
                char symbol = word[i];
                if (symbol != previousSymbol)
                    result.Append(symbol);
                previousSymbol = symbol;
            }

            // Print the result
            Console.WriteLine(result);
        }
    }
}