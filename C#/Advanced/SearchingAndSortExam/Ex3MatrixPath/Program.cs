// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex3MatrixPath
{
    internal class Program
    {
        private static bool[,] visited;
        private static List<int[]> matrix = new List<int[]>();
        
        public static void Main(string[] args)
        {
            int height = int.Parse(Console.ReadLine()!);
            int width = int.Parse(Console.ReadLine()!);
            visited = new bool[height, width];

            for (int i = 0; i < height; i++)
            {
                matrix.Add(
                Console.ReadLine()!
                    .Split()
                    .Select(int.Parse)
                    .ToArray()
                );
            }

            bool isTherePath = PathExists();

            Console.WriteLine(isTherePath 
                ? "Path 1..9 is found!"
                : "Path 1..9 is not found!");
        }
        public static bool PathExists()
        {
            if (FindPath(0, 0, 1))
            { 
                return true;
            }
            
            return false;
        }

        public static bool FindPath(int row, int col, int num)
        {
            if (row >= matrix.Count || row < 0 ||
                col >= matrix[1].Length || col < 0)
            {
                return false;
            }
            
            if (matrix[row][col] != num || visited[row, col])
            {
                return false;
            }
            
            if (matrix[row][col] == 9)
            {
                return true;
            }
            
            visited[row, col] = true;
            
            if (FindPath(row, col + 1, num + 1) ||
                FindPath(row, col - 1, num + 1) ||
                FindPath(row + 1, col, num + 1) ||
                FindPath(row - 1, col, num + 1))
            {
                return true;
            }
            
            visited[row, col] = false;
            return false;
        }
    }
}