using System;
using System.IO;

namespace Ex3_DFS_Traverse_Folders
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            DirectoryTraverserDFS(@"C:\Users\iparv\OneDrive\Desktop\Hackerrank");
        }

        public static void DirectoryTraverserDFS(string directoryPath)
        {
            DirectoryTraverserDFS(new DirectoryInfo(directoryPath), String.Empty);
        }
        public static void DirectoryTraverserDFS(DirectoryInfo dir, string spaces)
        {
            Console.WriteLine(spaces + dir.FullName);
            DirectoryInfo[] children = dir.GetDirectories();

            foreach (DirectoryInfo child in children)
            {
                DirectoryTraverserDFS(child, spaces + " ");
            }
        }
    }
}