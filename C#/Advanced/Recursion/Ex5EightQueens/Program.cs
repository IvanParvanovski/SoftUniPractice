using System;
using System.Collections.Generic;

namespace Ex5EightQueens
{
    internal class Program
    {
        const int Size = 8;
        static int[,] matrix = new int[Size, Size];

        static HashSet<int> attackedRows = new HashSet<int>();
        static HashSet<int> attackedCols = new HashSet<int>();
        static HashSet<int> attackedLeftDiagonals = new HashSet<int>();
        static HashSet<int> attackedRightDiagonals = new HashSet<int>();
        
        public static void Main(string[] args)
        {
            PlaceQueens(0);
        }

        private static void PlaceQueens(int row)
        {
            if (row == Size)
            {
                PrintSolution();
            }
            else
            {
                for (int col = 0; col < Size; col++)
                {
                    if (CanPlaceQueen(row, col))
                    {
                        MarkAttackedPosition(row, col);
                        PlaceQueens(row + 1);
                        UnMarkAttackedPositions(row, col);
                    }
                }
            }
        }

        private static void MarkAttackedPosition(int row, int col)
        {
            matrix[row, col] = 1;
            attackedRows.Add(row);
            attackedCols.Add(col);
            attackedLeftDiagonals.Add(col - row);
            attackedRightDiagonals.Add(col + row);
        }

        private static void UnMarkAttackedPositions(int row, int col)
        {
            matrix[row, col] = 0;
            attackedRows.Remove(row);
            attackedCols.Remove(col);
            attackedLeftDiagonals.Remove(col - row);
            attackedRightDiagonals.Remove(col + row);
        }

        private static bool CanPlaceQueen(int row, int col)
        {
            bool isFreePosition = attackedRows.Contains(row) 
                                  || attackedCols.Contains(col)
                                  || attackedLeftDiagonals.Contains(col - row)
                                  || attackedRightDiagonals.Contains(col + row);
            
            return !isFreePosition;
        }

        private static void PrintSolution()
        {
            for (int row = 0; row < Size; row++)
            {
                for (int col = 0; col < Size; col++)
                {
                    if (matrix[row, col] == 1)
                    {
                        Console.Write("* ");
                    }
                    else
                    {
                        Console.Write("- ");
                    }
                }
                Console.WriteLine();
            }
            Console.WriteLine();
        }
    }
}