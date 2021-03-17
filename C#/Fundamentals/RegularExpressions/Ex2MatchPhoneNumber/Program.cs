using System;
using System.Text.RegularExpressions;

namespace Ex2MatchPhoneNumber
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            string regexPattern = @"\+359(-| )2\1\d{3}\1\d{4}\b";
            Regex regex = new Regex(regexPattern);
            MatchCollection result = regex.Matches(text);
            Console.WriteLine(string.Join(", ", result));
        }
    }
}