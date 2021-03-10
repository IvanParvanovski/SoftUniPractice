using System;
using System.Text;

namespace Ex1ReverseStrings
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                string currentText = Console.ReadLine();
                if (currentText == "end")
                    break;
                
                Console.WriteLine($"{currentText} = {ReverseWord(currentText)}");
            }
        }
        private static string ReverseWord(string word)
        {
            StringBuilder result = new StringBuilder();
            foreach (char symbol in word)
                result.Insert(0, symbol);
            return result.ToString();
        }
    }
}