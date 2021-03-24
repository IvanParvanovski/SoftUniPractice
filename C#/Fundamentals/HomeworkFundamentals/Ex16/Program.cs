using System;
using System.Text.RegularExpressions;

namespace Ex16
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // <p>Please visit <a href="https://softuni.bg">our site</a> to choose a training course. Also visit <a href="www.devbg.org">our forum</a> to discuss the courses.</p>

            // Output:
            // <p>Please visit [URL=https://softuni.bg]our site[/URL] to choose a training course. Also visit [URL=www.devbg.org]our forum[/URL] to discuss the courses.</p>

            // Read user's input
            string text = Console.ReadLine();

            // Set up the regular expression
            string regexPattern = "<a href=\"(?<URL>.*?)\">(?<Text>.*?)<\\/a>";
            Regex regex = new Regex(regexPattern);

            // Replace each match with
            // [URL=match-url]match-text[/URL]

            string result = regex.Replace(text,
                match => $"[URL={match.Groups["URL"]}]" +
                         $"{match.Groups["Text"]}[/URL]");

            // Print the result
            Console.WriteLine(result);
        }
    }
}