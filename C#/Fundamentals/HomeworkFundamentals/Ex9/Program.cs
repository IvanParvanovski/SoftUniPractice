using System;
using System.Diagnostics;

namespace Ex9
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // Nakov
            // ab

            // Output:
            // \u002f\u0003\u000a\u000d\u0017

            // Read user's input and check if it is not empty or null.
            string text = Console.ReadLine();
            Debug.Assert(text != null, nameof(text) + " != null");

            string code = Console.ReadLine();
            Debug.Assert(code != null, nameof(code) + " != null");
            
            // Set up code's attributes
            int codeIndex = 0;
            int codeLength = code.Length;
            
            // Loop threw the text and code each character with the XOR operation
            // Between the TEXT character and CODE character
            // Print it with following zeros.
            foreach (char symbol in text)
            {
                if (codeLength <= codeIndex)
                    codeIndex = 0;
                
                Console.Write($"\\u{symbol ^ code[codeIndex]:x4}");
                codeIndex++;
            }
        }
    }
}