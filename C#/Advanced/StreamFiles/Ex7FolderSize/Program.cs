// See https://aka.ms/new-console-template for more information

using System;
using System.IO;

namespace FolderSize
{
    public class FolderSize
    {
        public static void Main(string[] args)
        {
            string folderPath = @"..\..\..\Files\";
            string outputPath = @"..\..\..\Files\output.txt";
            
            GetFolderSize(folderPath, outputPath);
        }

        public static void GetFolderSize(string folderPath, string outputFilePath)
        {
            var writer = new StreamWriter(outputFilePath);

            using (writer)
            {
                writer.WriteLine(GetSize(folderPath) + " KB");   
            }
        }

        public static double GetSize(string folderPath)
        {
            double currentSize = 0;
            
            var currentDir = new DirectoryInfo(folderPath);
            DirectoryInfo[] subDirs = currentDir.GetDirectories();
            FileInfo[] files = currentDir.GetFiles();

            foreach (FileInfo file in files)
            {
                currentSize += file.Length;
            }
            
            if (subDirs.Length == 0)
            {
                return currentSize;
            }

            foreach (var subDir in subDirs)
            {
                currentSize += GetSize(subDir.FullName);
            }

            return currentSize;
        }
    }
}