using System;
using System.Text.RegularExpressions;

namespace ExTest
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            Console.WriteLine(CountLetter(text, 'a'));
            
        }
        private static int CountLetter(string text, char ch)
        {
            int counter = 0;
            foreach (char symbol in text)
                if (symbol == ch)
                    counter++;

            return counter;
        }
    }
}