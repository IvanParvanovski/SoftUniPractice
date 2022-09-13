// See https://aka.ms/new-console-template for more information

using System;
using System.IO;

namespace LineNumbers
{
    public class LineNumbers
    {
        public static void Main(string[] args)
        {
            string inputFilePath = @"..\..\..\Files\text.txt";
            string outputFilePath = @"..\..\..\Files\output.txt";
            
            ProcessLines(inputFilePath, outputFilePath);
        }

        public static void ProcessLines(string inputFilePath, string outputFilePath)
        {
            var inputFile = new StreamReader(inputFilePath);
            var outputFile = new StreamWriter(outputFilePath);

            using (inputFile)
            using (outputFile)
            {
                int linesCounter = 1;
                string line = inputFile.ReadLine();
                
                while (line != null)
                {
                    int letters = 0;
                    int punctuationMarks = 0;

                    bool IsLowercaseLetter(char l) => l >= 'a' && l <= 'z';
                    bool IsUppercaseLetter(char l) => l >= 'A' && l <= 'Z';

                    foreach (var symbol in line)
                    {
                        if (IsLowercaseLetter(symbol) || IsUppercaseLetter(symbol))
                        {
                            letters++;
                        }
                        else if (symbol == ' ')
                        {
                            continue;
                        }
                        else
                        {
                            punctuationMarks++;
                        }
                    }
                    
                    outputFile.WriteLine($"Line {linesCounter}: {line} ({letters})({punctuationMarks})");
                    
                    line = inputFile.ReadLine();
                    linesCounter++;
                }
            }
        }
    }
}