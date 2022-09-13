// See https://aka.ms/new-console-template for more information

using System;
using System.IO;
using System.Linq;

namespace MergeFiles
{
    public class MergeFiles
    {
        public static void Main(string[] args)
        {
            string firstFile = Console.ReadLine();
            string secondFile = Console.ReadLine();
            string outputFile = @"..\..\..\Files\output.txt";
            
            MergeTextFiles(firstFile, secondFile, outputFile);
        }

        public static void MergeTextFiles(string firstInputFilePath, string secondInputFilePath, string outputFilePath)
        {
            string path = @"..\..\..\Files\";
            string[] firstFileWords = File.ReadAllLines(path + firstInputFilePath);
            string[] secondFileWords = File.ReadAllLines(path + secondInputFilePath);
            
            var writer = new StreamWriter(outputFilePath);
            
            string[] collectionWithMoreWords;
            string[] collectionWithLessWords;
            
            if (firstFileWords.Length < secondFileWords.Length)
            {
                collectionWithLessWords = firstFileWords;
                collectionWithMoreWords = secondFileWords;
            }
            else
            {
                collectionWithLessWords = secondFileWords;
                collectionWithMoreWords = firstFileWords;
            }
            
            using (writer)
            {
                int i = 0;
                for (; i < collectionWithLessWords.Length; i++)
                {
                    writer.WriteLine(firstFileWords[i]);
                    writer.WriteLine(secondFileWords[i]);
                }

                for (; i < collectionWithMoreWords.Length; i++)
                {
                    writer.WriteLine(collectionWithMoreWords[i]);
                }
            }
        }
    }
}