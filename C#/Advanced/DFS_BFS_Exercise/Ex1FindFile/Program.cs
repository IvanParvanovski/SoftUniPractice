// See https://aka.ms/new-console-template for more information

using System;
using System.IO;
using System.Linq;

namespace Ex1FindFile
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            TraverseDirDFS(@"C:\", "shkolo.png");
        }

        private static void TraverseDirDFS(string dirPath, string fileName)
        {
            TraverseDirDFS(new DirectoryInfo(dirPath), fileName);
        }
        private static void TraverseDirDFS(DirectoryInfo dir, string fileName)
        {
            try
            {
                var other = dir.GetDirectories();
                var files = dir.GetFiles().Select(f => f.Name);

                if (files.Contains(fileName))
                {
                    Console.WriteLine($"{fileName} is found in {dir.FullName}");
                }

                foreach (var r in other)
                {
                    TraverseDirDFS(r, fileName);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine($"No access to {dir}");
            }
            
        }
    }
}
