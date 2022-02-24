using System;
using System.Collections.Generic;

namespace Ex6MagicSquares
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int[][] matrix =
            {
                new int[3],
                new int[3],
                new int[3],
            };
            
            MagicSquares(matrix, 0, 0);
        }

        public static void MagicSquares(
            int[][] matrix,
            int rowIndex, 
            int colIndex)
        {
            if (colIndex == 3)
            {
                rowIndex += 1;
                colIndex = 0;
            }
            
            if (rowIndex == 3)
            {
                foreach (int[] sequence in matrix)
                {
                    Console.WriteLine(String.Join(" ", sequence));
                }

                Console.WriteLine();
                return;
            }

            for (int i = 1; i < 10; i++)
            {
                matrix[rowIndex][colIndex] = i;
                MagicSquares(matrix, rowIndex, colIndex + 1);
            }

        }
    }
}