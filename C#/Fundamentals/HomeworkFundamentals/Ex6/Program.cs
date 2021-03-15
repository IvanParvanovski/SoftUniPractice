using System;
using System.Text.RegularExpressions;

namespace Ex6
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            string regexPattern = @"(?<=<upcase>)(.*?)(?=<\/upcase>)";
            
            Regex regex = new Regex(regexPattern);
            MatchCollection matches = regex.Matches(text!);
            
            string result = text;
            foreach (Match match in matches)
            {
                string word = match.ToString();
                string currentPattern = @"<upcase>" + word + @"<\/upcase>";
                result = Regex.Replace(result, currentPattern, word.ToUpper());
            }

            Console.WriteLine(result);
        }
    }
}