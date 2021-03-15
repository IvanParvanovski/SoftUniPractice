using System;
using System.Text.RegularExpressions;

namespace Ex19
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            string regexPattern = @"([a-zA-Z]{2,}[0-9]*\.)*[a-zA-Z]{2,}[0-9]*@[a-zA-Z]+[0-9]*(\.[a-zA-Z]+)+";
            Regex regex = new Regex(regexPattern);
            MatchCollection emails = regex.Matches(text!);
            foreach (Match email in emails)
                Console.WriteLine(email);
        }
    }
}