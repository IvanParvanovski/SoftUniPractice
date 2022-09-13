// See https://aka.ms/new-console-template for more information

using System;
using System.IO;
using System.Text;

namespace CopyBinaryFile
{
    public class CopyBinaryFile
    {
        public static void Main(string[] args)
        {
            string imgPath = @"..\..\..\logo.png";
            string copyImgPath = @"..\..\..\copyLogo.png";

            CopyFile(imgPath, copyImgPath);
        }

        public static void CopyFile(string inputFilePath, string outputFilePath)
        {
            var imgFile = new FileStream(inputFilePath, FileMode.Open);
            var copyImgFile = new FileStream(outputFilePath, FileMode.Create);
            
            using (imgFile)
            using (copyImgFile)
            {
                int bytesRead = 0;
                byte[] buffer = new byte[4096];

                while ((bytesRead = imgFile.Read(buffer, 0, buffer.Length)) > 0)
                {
                    copyImgFile.Write(buffer, 0, bytesRead);
                }
            }
        }
    }
}
