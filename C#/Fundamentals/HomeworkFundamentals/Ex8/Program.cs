using System;
using System.Text;

namespace Ex8
{
    class Program
    {
        static void Main(string[] args)
        {
            // Не знам как да прочета unicode текст от конзолата.
            
            string text = Console.ReadLine();
            for (int i = 0; i < text.Length; i++)
                Console.Write($"\\u{Char.ConvertToUtf32(text, i):x4}");
        }
    }
}