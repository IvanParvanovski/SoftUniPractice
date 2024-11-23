namespace Sudoku
{
    public class Program
    {
        public static char[][] matrix = new char[9][];

        public static void Main(string[] args)
        {
            //string input = Console.ReadLine();
            //// ["5","3",".",".","7",".",".",".","."]
            //List<List<char>> board = new List<List<char>>();

            //while (input != "End")
            //{
            //    List<char> row = new List<char>();

            //    foreach (char symbol in input)
            //    {
            //        if (char.IsDigit(symbol) || symbol == '.')
            //        {
            //            row.Add(symbol);
            //        }
            //    }

            //    board.Add(row);
            //    input = Console.ReadLine();
            //}

            //Console.WriteLine("hi");

            ReadMatrix();
            Console.WriteLine("hi");

            CheckRows();
        }

        public static void ReadMatrix()
        {
            string input = Console.ReadLine();

            for (int r = 0; r < 9; r++)
            {
                if (input == "End")
                {
                    break;
                }

                char[] currentRow = new char[9];
                int index = 0;

                foreach (char symbol in input)
                {
                    if (char.IsDigit(symbol) || symbol == '.')
                    {
                        currentRow[index] = symbol;
                        index++;
                    }
                }

                matrix[r] = currentRow;
                input = Console.ReadLine();
            }
        }

        public static bool CheckRows(char[][] board)
        {
            for (int i = 0; i < board.Length; i++)
            {
                HashSet<char> set = new HashSet<char>();

                for (int j = 0; j < board[i].Length; j++)
                {
                    if (set.Contains(matrix[i][j]) && board[i][j] != '.')
                    {
                        return false;
                    }
                }
            }


            return false;
        }

        public static bool CheckSquare(char[][] board)
        {
            return true;
        }
    }
}
