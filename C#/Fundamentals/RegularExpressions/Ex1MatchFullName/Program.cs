using System;
using System.Text.RegularExpressions;

namespace Ex1MatchFullName
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            string regexPattern = @"\b[A-Z][a-z]+ [A-Z][a-z]+\b";
            Regex regex = new Regex(regexPattern);
            MatchCollection result = regex.Matches(text!);
            Console.WriteLine(String.Join('\n', result));
        }
    }
}
