using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex3MatrixPath
{
    class Node 
    {
        public int Value {get; set;}
        public int Row { get; set; }
        public int Col { get; set; }
    }
    
    internal class Program
    {
        private static List<int[]> matrix;
        private static bool isChange = false;
        
        public static void Main(string[] args)
        {
            int height = int.Parse(Console.ReadLine()!);
            int width = int.Parse(Console.ReadLine()!);
            
            matrix = new List<int[]>();
            
            for (int i = 0; i < height; i++)
            {
                int[] currentRow = Console.ReadLine()
                    .Split()
                    .Select(int.Parse)
                    .ToArray();

               matrix.Add(currentRow);
            }
            
            Node current = new Node();
            current.Col = 0;
            current.Row = 0;
            current.Value = matrix[0][0];

            bool isTherePath = SearchPath(current);

            if (isTherePath)
            {
                Console.WriteLine("There is a path!");
            }
            else
            {
                Console.WriteLine("No path!");
            }
        }

        public static bool SearchPath(Node current)
        {
            TryDirection(current, current.Row + 1, current.Col - 1);
            TryDirection(current, current.Row + 1, current.Col);
            TryDirection(current, current.Row + 1, current.Col + 1);

            if (current.Row == matrix.Count - 1)
            {
                isChange = true;
                return true;
            }

            return false;
        }

        private static void TryDirection(Node current, int nextRow, int nextCol)
        {
            if (isChange)
            {
                return;
            }
            
            if (nextRow < matrix.Count 
                && nextCol < matrix.Count && nextCol >= 0 
                && current.Value < matrix[nextRow][nextCol])
            {
                current.Value = matrix[nextRow][nextCol];
                current.Row = nextRow;
                current.Col = nextCol;
                SearchPath(current);
            }
        }
    
        
       
    }
}
