// See https://aka.ms/new-console-template for more information

using System;
using System.IO;
using System.Linq;

namespace ExtractBytes
{
    public class ExtractBytes
    {
        public static void Main(string[] args)
        {
            string imgPath = @"..\..\..\Files\logo.png";
            string bytesTxtPath = @"..\..\..\Files\bytes.txt";
            string outputPath = @"..\..\..\Files\output.bin";
            
            ExtractBytesFromBinaryFile(imgPath, bytesTxtPath, outputPath);
        }

        public static void ExtractBytesFromBinaryFile(string binaryFilePath, string bytesFilePath, string outputPath)
        {
            byte[] searchedBytes = File.ReadAllLines(bytesFilePath).Select(byte.Parse).ToArray();
            byte[] binaryFile = File.ReadAllBytes(binaryFilePath);
            
            var writer = new StreamWriter(outputPath);
            
            using (writer)
            {
                foreach (byte b in binaryFile)
                {
                    if (searchedBytes.Contains(b))
                    {
                        writer.WriteLine(b);
                    }
                }
            }
        }
    }
}