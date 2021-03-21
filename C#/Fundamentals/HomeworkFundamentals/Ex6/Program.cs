using System;
using System.Text.RegularExpressions;

namespace Ex6
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // We are living in a <upcase>yellow submarine</upcase>. We don't have <upcase>anything</upcase> else.
            
            // Output:
            // We are living in a YELLOW SUBMARINE. We don't have ANYTHING else.
            
            // Read the user's input.
            string text = Console.ReadLine();
            
            // Set up the regular expression.
            string regexPattern = @"<upcase>(?<insideText>.*?)<\/upcase>";
            Regex regex = new Regex(regexPattern);
            
            // Replace all of the matches
            // With the text inside of each match with capitalized letters.
            string result = regex.Replace(text!,
                                   match => match.Groups["insideText"].Value.ToUpper());
            
            // Print the stdout
            Console.WriteLine(result);
        }
    }
}