using System;
using System.Text.RegularExpressions;

namespace Ex20
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // I was born at 14.06.1980. My sister was born at 3.7.1984. In 5/1999 I graduated my high school. The law says (see section 7.3.12) that we are allowed to do this (section 7.4.2.9).
            
            // Read user's input
            string text = Console.ReadLine();

            // Set up the regular expression
            string regexPattern = @"\d+\.\d+\.[0-9]{4}";
            Regex regex = new Regex(regexPattern);
            
            // Get all of the dates in the text
            MatchCollection dates = regex.Matches(text);
            
            // Print all of the matching dates
            Console.WriteLine(string.Join('\n', dates));
        }
    }
}