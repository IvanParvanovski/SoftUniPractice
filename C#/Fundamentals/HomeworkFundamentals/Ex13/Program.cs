using System;
using System.Text.RegularExpressions;

namespace Ex13
{
    class Program
    {
        static void Main(string[] args)
        {
            string url = Console.ReadLine();
            string regexPattern = @"(?<protocol>[a-zA-Z]+):\/\/(?<server>(\w+\.)+\w+)\/(?<resource>.*)";
            Regex regex = new Regex(regexPattern);
            Match result = regex.Match(url);
            Console.WriteLine($"[protocol]={result.Groups["protocol"]}\n" +
                              $"[server]={result.Groups["server"]}\n" +
                              $"[resource]={result.Groups["resource"]}");
        }
    }
}