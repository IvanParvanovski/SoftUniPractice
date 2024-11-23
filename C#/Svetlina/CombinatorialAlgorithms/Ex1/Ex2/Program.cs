namespace Ex2
{
    public class Program
    {
        public static void Main(string[] args)
        {

        }

        public static void GenerateCombinations(int n, int k)
        {
            var combinations = new List<List<int>>();


        }

        private static void Backtracking(int start, List<int> current, List<List<int>> results, int n, int k)
        {
            if (current.Count == k)
            {
                results.Add(new List<int>(current));
                return;
            }


        }
    }
}