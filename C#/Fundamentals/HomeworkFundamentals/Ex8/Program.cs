using System;
using System.Text;

namespace Ex8
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // Наков -> \u041d\u0430\u043a\u043e\u0432
            // Nakov -> \u004e\u0061\u006b\u006f\u0076

            // Set up the console so it can read Unicode characters.
            Console.InputEncoding = Encoding.Unicode;
            Console.OutputEncoding = Encoding.Unicode;
            
            // Read user's input.
            string text = Console.ReadLine();
            
            // Go threw each character in the text
            // Convert it to hexadecimal with following zeros
            // Print it on the shell
            for (int i = 0; i < text.Length; i++)
                Console.Write($"\\u{Char.ConvertToUtf32(text, i):x4}");
        }
    }
}