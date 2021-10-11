using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Ex3Test
{
    class Program
    {
        static void Main(string[] args)
        {
            int amountOfFiles = int.Parse(Console.ReadLine());
            
            string regexPattern = @"(?<root>\w+)\\(\w+\\)+(?<file>\w+\.\w+);(?<fileSize>\d+)";
            Regex regex = new Regex(regexPattern);
            Dictionary<string, Dictionary<string, long>> files = new Dictionary<string, Dictionary<string, long>>();
            
            for (int i = 0; i < amountOfFiles; i++)
            {
                string currentFile = Console.ReadLine();
                Match match = regex.Match(currentFile);
                if (match.Success)
                {
                    string root = match.Groups["root"].ToString();
                    string file = match.Groups["file"].ToString();
                    long fileSize = long.Parse(match.Groups["fileSize"].ToString());

                    if (!files.ContainsKey(root))
                    {
                        files[root] = new Dictionary<string, long>();
                    }

                    files[root][file] = fileSize;
                }
            }

            string[] searchedFiles = Console.ReadLine().Split(" ");
            string searchedExtension = searchedFiles[0];
            string searchedDir = searchedFiles[2];

            if (files.ContainsKey(searchedDir))
            {
                Dictionary<string, long> wantedDir = files[searchedDir];
                Dictionary<string, long> result = new Dictionary<string, long>();
            
                foreach (var file in wantedDir)
                {
                    if (file.Key.EndsWith(searchedExtension))
                    {
                        result[file.Key] = file.Value;
                    }
                }
            
                foreach (var element in result.OrderByDescending(x => x.Value).ThenBy(x => x.Key))
                {
                    Console.WriteLine($"{element.Key} - {element.Value} KB");
                }
            }
            else
            {
                Console.WriteLine("No");
            }
            
        }
    }
}