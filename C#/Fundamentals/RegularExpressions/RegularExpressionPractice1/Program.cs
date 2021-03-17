using System;
using System.Text.RegularExpressions;

namespace RegularExpressionPractice1
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = "Nakov: 123";
            string pattern = @"([A-Z][a-z]+): (\d+)";
            Regex regex = new Regex(pattern);
            Match match = regex.Match(text);
            
        }
    }
}