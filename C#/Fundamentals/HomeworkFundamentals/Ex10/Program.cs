using System;
using System.Text.RegularExpressions;

namespace Ex10
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] sentences = Console.ReadLine()?.Split(". ");
            string searchedWord = Console.ReadLine();

            string regexPattern = @"\b" + searchedWord + @"\b";
            Regex regex = new Regex(regexPattern);
            foreach (string sentence in sentences)
                if (regex.IsMatch(sentence))
                    Console.WriteLine(sentence);
            
        }
    }
}