// See https://aka.ms/new-console-template for more information

using System;
using System.IO;
using System.Text;
using Microsoft.VisualBasic.FileIO;

namespace CopyDirectory
{
    public class CopyDirectory
    {
        public static void Main(string[] args)
        {
            string path = @"C:\Users\iparv\OneDrive\Desktop\SoftUni\C#\Advanced\StreamFiles\Ex5CopyDirectoryContents\";
            
            string copyFolderPath = path + @"copyDirectory\";
            string mainFolderPath = path + @"mainDirectory\";
            
            CopyAllFiles(mainFolderPath, copyFolderPath);
        }
        
        public static void CopyAllFiles(string inputPath, string outputPath)
        {
            if (Directory.Exists(outputPath))
            {
                Directory.Delete(outputPath, true);
            }
            Directory.CreateDirectory(outputPath);

            string[] filesMainDir = Directory.GetFiles(inputPath);

            foreach (string file in filesMainDir)
            {
                string fileContent = File.ReadAllText(file);
                File.WriteAllText(outputPath + GetFileName(file), fileContent);
            }
        }

        public static string GetFileName(string file)
        {
            int lastSlashIndex = file.LastIndexOf("\\");
            StringBuilder sb = new StringBuilder();

            for (int i = lastSlashIndex; i < file.Length; i++)
            {
                sb.Append(file[i]);
            }

            return sb.ToString();
        }
    }
}