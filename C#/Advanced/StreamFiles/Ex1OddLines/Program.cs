// See https://aka.ms/new-console-template for more information

using System.IO;

namespace OddLines
{
    public class OddLines
    {
        public static void Main(string[] args)
        {
            string inputFilePath = @"..\..\..\Files\input.txt";
            string outputFilePath = @"..\..\..\Files\output.txt";
            
            ExtractOddLines(inputFilePath, outputFilePath);
        }

        public static void ExtractOddLines(string inputFilePath, string outputFilePath)
        {
            var inputFile = new StreamReader(inputFilePath);
            var outputFile = new StreamWriter(outputFilePath);

            using (inputFile)
            {
                int counter = 0;
                string line = inputFile.ReadLine();

                using (outputFile)
                {
                    while (line != null)
                    {
                        if (counter % 2 == 1)
                        {
                            outputFile.WriteLine(line);
                        }

                        counter++;
                        line = inputFile.ReadLine();
                    }
                }
            }
        }
    }
}
