using System;
using System.Linq;

namespace Ex5
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            string subText = Console.ReadLine();
            Console.WriteLine(CountWord(text, subText));
        }

        private static int CountWord(string text, string subText)
        {
            text = text.ToLower();
            subText = subText.ToLower();
            
            int index = text.IndexOf(subText, StringComparison.Ordinal);
            int counter = 0;
            while (index != -1)
            {
                counter++;
                index = text.IndexOf(subText, index + 1, StringComparison.Ordinal);
            }

            return counter;
        }
    }
}