using System;
using System.Text.RegularExpressions;

namespace Ex3MatchDates
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            string regexPattern = @"\b(?<day>\d{2})(\/|\.|-)(?<month>[A-Z][a-z]{2})\1(?<year>\d{4})\b";
            // string regexPattern = @"\b(?<day>\d{2})(?<separator>[-.\/])(?<month>[A-Z][a-z]{2})\2(?<year>\d{4})\b";
            Regex regex = new Regex(regexPattern);
            MatchCollection result = regex.Matches(text!);
            
            foreach (Match match in result)
                Console.WriteLine($"Day: {match.Groups["day"].Value}, " +
                                  $"Month: {match.Groups["month"].Value}, " +
                                  $"Year: {match.Groups["year"].Value}");
        }
    }
}