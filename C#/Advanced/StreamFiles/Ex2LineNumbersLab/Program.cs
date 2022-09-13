// See https://aka.ms/new-console-template for more information

using System;
using System.IO;


namespace LineNumbers
{
    public class LineNumbers
    {
        public static void Main(string[] args)
        {
            string inputFilePath = @"..\..\..\Files\input.txt";
            string outputFilePath = @"..\..\..\Files\output.txt";
            
            RewriteFileWithLineNumbers(inputFilePath, outputFilePath);
        }

        public static void RewriteFileWithLineNumbers(string inputFilePath, string outputFilePath)
        {
            var reader = new StreamReader(inputFilePath);
            var writer = new StreamWriter(outputFilePath);
            
            using (reader)
            using (writer)
            {
                string line = reader.ReadLine()!;
                int counter = 1;
                
                while (line != null)
                {
                    writer.WriteLine($"{counter}. {line}");
                    
                    line = reader.ReadLine()!;
                }
            }
        }
    }
}