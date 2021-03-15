using System;
using System.Text.RegularExpressions;

namespace Ex16
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            string regexPattern = "<a href=\"(?<URL>.*?)\">(?<Text>.*?)<\\/a>";
            Regex regex = new Regex(regexPattern);
            MatchCollection matches = regex.Matches(text);

            string result = text;
            foreach (Match link in matches)
            {
                string url = link.Groups["URL"].ToString();
                string linkText = link.Groups["Text"].ToString();
                string currentPattern = "<a href=\"" + url + "\">"+ linkText +"<\\/a>";
                string newText = $"[URL={url}]{linkText}[/URL]";
                result = Regex.Replace(result, currentPattern, newText);
            }

            Console.WriteLine(result);
        }
    }
}
