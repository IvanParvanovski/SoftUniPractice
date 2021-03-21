using System;
using System.Text.RegularExpressions;

namespace Ex13
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // http://www.devbg.org/forum/index.php
            
            // Output:
            // [protocol]="http"
            // [server]="www.devbg.org"
            // [resource]="/forum/index.php"
            
            // Read url
            string url = Console.ReadLine();
            
            // Set up the regular expression
            string regexPattern = @"(?<protocol>[a-zA-Z]+):\/\/(?<server>(\w+\.)+\w+)\/(?<resource>.*)";
            Regex regex = new Regex(regexPattern);
            
            // Check if url matches and print the result
            Match result = regex.Match(url);
            Console.WriteLine($"[protocol]=\"{result.Groups["protocol"]}\"\n" +
                              $"[server]=\"{result.Groups["server"]}\"\n" +
                              $"[resource]=\"{result.Groups["resource"]}\"");
        }
    }
}