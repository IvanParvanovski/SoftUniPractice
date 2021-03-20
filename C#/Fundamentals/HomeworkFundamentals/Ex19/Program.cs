using System;
using System.Text.RegularExpressions;

namespace Ex19
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // Please contact us by phone (+359 222 222 222) or by email at example@abv.bg or at baj.ivan@yahoo.co.uk. This is not email: test@test. This also: @softuni.bg.com. Neither this: a@a.b.
            
            // Read user's input
            string text = Console.ReadLine();
            
            // Set up the regular expression
            string regexPattern = @"([a-zA-Z]{2,}[0-9]*\.)*[a-zA-Z]{2,}[0-9]*@[a-zA-Z]+[0-9]*(\.[a-zA-Z]+)+";
            Regex regex = new Regex(regexPattern);
            
            // Get all valid emails
            MatchCollection emails = regex.Matches(text!);
            
            // Print the result
            Console.WriteLine(string.Join('\n', emails));
        }
    }
}