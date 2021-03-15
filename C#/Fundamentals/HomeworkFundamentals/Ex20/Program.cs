using System;
using System.Text.RegularExpressions;

namespace Ex20
{
    class Program
    {
        static void Main(string[] args)
        {
            string regexPattern = @"\d+\.\d+\.[0-9]{4}";
            Regex regex = new Regex(regexPattern);
            string text = Console.ReadLine();
            MatchCollection dates = regex.Matches(text);
            
            foreach (Match date in dates)
                Console.WriteLine(date);
                
            
        }
    }
}