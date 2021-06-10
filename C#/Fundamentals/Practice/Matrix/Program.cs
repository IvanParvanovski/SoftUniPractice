using System;

namespace Matrix
{
    class Program
    {
        static void Main(string[] args)
        {
            Random random = new Random();
            int[,] matrix = new int[10 , 10];
            for (int row = 0; row < matrix.GetLength(0); row++)
            {
                for (int col = 0; col < matrix.GetLength(1); col++)
                {
                    matrix[row, col] = random.Next(1, 10);
                    Console.Write(matrix[row, col]);
                }
                
                Console.WriteLine();
            }
        }
    }
}