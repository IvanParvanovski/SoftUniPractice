// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace DirectoryTraversal
{
    public class DirectoryTraversal
    {
        public static void Main(string[] args)
        {
            string path = Console.ReadLine();
            WriteReportToDesktop(
                TraverseDirectory(path), 
                "report"
            );
        }
        
        public static string TraverseDirectory(string inputFolderPath)
        {
            string path = @"..\..\..\" + inputFolderPath;
            DirectoryInfo dir = new DirectoryInfo(path);
            FileInfo[] files = dir.GetFiles("*");
            List<string> output = new List<string>();

            var extensions = files
                .GroupBy(x => x.Extension)
                .ToDictionary(
                    y => y.Key, 
                    y=> y.Count())
                .OrderByDescending(z => z.Value)
                .ThenBy(x => x.Key);

            foreach (var extensionItem in extensions)
            {
                string extension = extensionItem.Key;
                output.Add(extension);
                
                FileInfo[] currentFiles = files.Where(x => x.Extension == extension).ToArray();
                var sortedFiles = currentFiles.OrderBy(x => x.Length);

                foreach (var sf in sortedFiles)
                {
                    output.Add($"--{sf.Name}{sf.Extension} - {sf.Length}kb");
                }
            }

            return String.Join("\n", output);
        }

        public static void WriteReportToDesktop(string textContent, string reportFileName)
        {
            string desktopPath = Environment.GetFolderPath(Environment.SpecialFolder.DesktopDirectory);
            string fullPath = $@"{desktopPath}\{reportFileName}.txt";
            StreamWriter outputFile = new StreamWriter(fullPath);

            using (outputFile)
            {
                outputFile.Write(textContent);
            }
            
        }
    }
}