namespace ExCombinationsNtoK
{
    public class Program
    {
        public static int fullIterations = 0;

        public static void Main(string[] args)
        {
            int n = 4;
            int k = 2;

            int[] input = Enumerable.Range(1, n).ToArray();
            int[] currentNumbers = new int[k];
            var isUsed = new HashSet<int>();
            var result = new List<int[]>();

            GenerateCombinations(0, k, input, currentNumbers, isUsed, result);
        }

        public static void GenerateCombinations(int depth, int spots, int[] input, int[] currentNumbers, HashSet<int> isUsed, List<int[]> result)
        {
            if (depth == spots)
            {
                Console.WriteLine(String.Join(" ", currentNumbers));
                result.Add(currentNumbers);
                return;
            }

            for (int i = fullIterations; i < input.Length; i++)
            {
                int number = input[i];

                if (!isUsed.Contains(number))
                {
                    currentNumbers[depth] = number;
                    isUsed.Add(number);

                    GenerateCombinations(depth + 1, spots, input, currentNumbers, isUsed, result);
                    isUsed.Remove(number);

                    if (depth == 0)
                    {
                        fullIterations += 1;
                    }
                }
            }
        }
    }
}