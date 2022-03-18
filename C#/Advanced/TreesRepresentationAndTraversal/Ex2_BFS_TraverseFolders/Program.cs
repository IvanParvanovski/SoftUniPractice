using System;
using System.Collections.Generic;
using System.IO;

namespace Ex2_BFS_TraverseFolders
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            DirectoryTraverserBFS(@"C:\Users\iparv\OneDrive\Desktop\Harvard\CS50_AI");
        }
        public static void DirectoryTraverserBFS(string directoryPath)
        {
            var visitedDirsQueue = new Queue<DirectoryInfo>();
            visitedDirsQueue.Enqueue(new DirectoryInfo(directoryPath));
            
            while (visitedDirsQueue.Count > 0)
            {
                DirectoryInfo currentDir = visitedDirsQueue.Dequeue();
                Console.WriteLine(currentDir.FullName);

                foreach (DirectoryInfo child in currentDir.GetDirectories())
                {
                    visitedDirsQueue.Enqueue(child);
                }
            }
        }
    }
}