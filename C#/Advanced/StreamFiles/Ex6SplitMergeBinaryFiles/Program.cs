// See https://aka.ms/new-console-template for more information

using System;
using System.IO;
using System.Linq;
using System.Text;

namespace SplitMergeBinaryFile
{
    public class SplitMergeBinaryFile
    {
        public static void Main(string[] args)
        {
            string partOnePath = @"..\..\..\Files\part-1.bin";
            string partTwoPath = @"..\..\..\Files\part-2.bin";
            string imgPath = @"..\..\..\Files\logo.png";
            string copiedPath = @"..\..\..\Files\example-joined.png";
            
            SplitBinaryFile(imgPath, partOnePath, partTwoPath);
            MergeBinaryFiles(partOnePath, partTwoPath, copiedPath);
        }

        public static void SplitBinaryFile(string sourceFilePath, string partOneFilePath, string partTwoFilePath)
        {
            byte[] bytes = File.ReadAllBytes(sourceFilePath);
            
            var firstFile = new StreamWriter(partOneFilePath);
            var secondFile = new StreamWriter(partTwoFilePath);
            
            int i = 0;
            
            using (firstFile)
            {
                for (; i < (bytes.Length + 1) / 2; i++)
                {
                    firstFile.WriteLine(bytes[i]);
                }
            }

            using (secondFile)
            {
                for (; i < bytes.Length; i++)
                {
                    secondFile.WriteLine(bytes[i]);
                }
            }
        }

        public static void MergeBinaryFiles(string partOneFilePath, string partTwoFilePath, string joinedFilePath)
        {
            var firstFile = new FileStream(partOneFilePath, FileMode.Open);
            var secondFile =  new FileStream(partTwoFilePath, FileMode.Open);
            var mergedFile = new FileStream(joinedFilePath, FileMode.Create);
            
            using (firstFile)
            using (secondFile)
            using (mergedFile)
            {
                int bytesRead = 0;
                byte[] buffer = new byte[4096];

                while ((bytesRead = firstFile.Read(buffer, 0, buffer.Length)) > 0)
                {
                    mergedFile.Write(buffer, 0, bytesRead);
                }
                
                while ((bytesRead = secondFile.Read(buffer, 0, buffer.Length)) > 0)
                {
                    mergedFile.Write(buffer, 0, bytesRead);
                }
            }
        }
    }
}