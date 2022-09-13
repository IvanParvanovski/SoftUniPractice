// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace WordCount
{
    public class WordCount
    {
        public static void Main(string[] args)
        {
            string wordsPath = @"..\..\..\Files\words.txt";
            string inputPath = @"..\..\..\Files\text.txt";
            string outputPath = @"..\..\..\Files\output.txt";

            CalculateWordCounts(wordsPath, inputPath, outputPath);
        }

        public static void CalculateWordCounts(string wordsFilePath, string textFilePath, string outputFilePath)
        {
            Dictionary<string, int> words = File.ReadAllText(wordsFilePath).Split(" ").ToDictionary(
                x => x,  x => 0);
            
            var reader = new StreamReader(textFilePath);
            var writer = new StreamWriter(outputFilePath);

            using (reader)
            {
                string line = reader.ReadLine();

                while (line != null)
                {
                    string[] keys = words.Keys.ToArray();
                    foreach (var word in keys)
                    {
                        int i = 0;

                        while (true)
                        {
                            i = line.IndexOf(word, i);
                            if (i == -1) { break; }
                            
                            i++;
                            words[word] += 1;
                        }
                    }

                    line = reader.ReadLine();
                }
            }

            using (writer)
            {
                foreach (var kvp in words.OrderByDescending(x => x.Value))
                {
                    writer.WriteLine($"{kvp.Key} - {kvp.Value}");
                }
            }
        }
    }
}