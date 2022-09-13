// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace EvenLines
{
    public class EvenLines
    {
        static void Main()
        {
            string inputFilePath = @"..\..\..\text.txt";
            Console.WriteLine(ProcessLines(inputFilePath));
        }
        public static string ProcessLines(string inputFilePath)
        {
            List<string> output = new List<string>();
            
            using (var reader = new StreamReader(inputFilePath))
            {
                int counter = 0;
                var line = reader.ReadLine();
                
                while (line != null)
                {
                    StringBuilder lineBuilder = new StringBuilder();
                    for (int i = 0; i < line.Length; i++)
                    {
                        char symbol = line[i];
                        lineBuilder.Append(GetSymbol(symbol));
                    }

                    string encodedLine = lineBuilder.ToString();
                    string reversedWords = String.Join(
                        " ", encodedLine.Split(" ").Reverse()
                    );
                    
                    if (counter % 2 == 0) { output.Add(reversedWords); }

                    line = reader.ReadLine();
                    counter++;
                }
            }

            return String.Join("\n", output);
        }

        public static char GetSymbol(char symbol)
        {
            if (symbol == '-' ||
                symbol == ',' ||
                symbol == '.' ||
                symbol == '!' ||
                symbol == '?')
            {
                return '@';
            }

            return symbol;
        }
    }
}