using System;
using System.Diagnostics;

namespace Ex9
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            string code = Console.ReadLine();

            int codeIndex = 0;
            Debug.Assert(code != null, nameof(code) + " != null");
            int codeLength = code.Length;
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