using System;
using System.Linq;

namespace Ex2PascalTriangle
{
    class Program
    {
        static void Main(string[] args)
        {
            int num = Int32.Parse(Console.ReadLine());
            int[] lastRow = { 1 };
            Console.WriteLine(lastRow.ElementAtOrDefault(0));

            for (int row = 2; row <= num; row++)
            {
                int[] currentRow = new int[row];
                for (int col = 0; col < row; col++)
                    currentRow[col] = lastRow.ElementAtOrDefault(col - 1) +
                                      lastRow.ElementAtOrDefault(col); 
                lastRow = currentRow;
                Console.WriteLine(string.Join(' ', currentRow));
            }
        }

    }
}
