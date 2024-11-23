namespace Ex3Exam
{
    public class Program
    {
        public static List<List<char>> matrix = new List<List<char>>();

        public static void Main(string[] args)
        {
            int rows = 4;
            int cols = 6;
            //int rows = 4;
            //int cols = 4;

            ReadMatrix(rows);
            Console.WriteLine(GetTunnelsCount(rows, cols));
        }

        public static void ReadMatrix(int r)
        {
            for (int i = 0; i < r; i++)
            {
                matrix.Add(Console.ReadLine().ToList());
            }
        }

        public static int SearchHorizontal()
        {
            int count = 0;

            for (int r = 0; r < matrix.Count(); r++)
            {
                List<char> currentRow = matrix[r];

                count += SearchLine(currentRow) ? 1 : 0;
            }

            return count;
        }

        public static int SearchVertical(int rows, int cols)
        {
            int count = 0;
            
            for (int c = 0; c < cols; c++)
            {
                List<char> currentRow = new List<char>();
                for (int r = 0; r < rows; r++)
                {
                    currentRow.Add(matrix[r][c]);
                }

                count += SearchLine(currentRow) ? 1 : 0;
            }

            return count;

        }

        public static bool SearchLine(List<char> currentRow)
        {
            for (int c = 0; c < currentRow.Count(); c++)
            {
                char currentSymbol = currentRow[c];

                if (currentSymbol == 'd')
                {
                    return false;
                }
            }

            return true;
        }

        public static int GetTunnelsCount(int rows, int cols)
        {
            return SearchHorizontal() + SearchVertical(rows, cols);
        }

    }
}