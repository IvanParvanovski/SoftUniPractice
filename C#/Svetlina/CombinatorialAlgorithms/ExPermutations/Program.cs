namespace ExPermutations
{
    public class Program
    {
        public static List<int[]> results = new List<int[]>();

        public static void Main(string[] args)
        {

            var numbers = new int[] { 1, 2, 3 };
            var currentNumbers = new int[numbers.Length];
            var isUsed = new HashSet<int>();

            GeneratePermutations(0, numbers, currentNumbers, isUsed);

            Console.WriteLine("hi");

            foreach (var r in results)
            {
                Console.WriteLine(r);
                Console.WriteLine(string.Join(" ", r));
            }
        }

        public static void GeneratePermutations(int depth, int[] input, int[] currentNumbers, HashSet<int> isUsed)
        {
            if (depth == input.Length)
            { 
                Console.WriteLine(string.Join(" ", currentNumbers));

                results.Append(currentNumbers.ToArray());
            }

            for (int i = 0; i < input.Length; i++)
            {
                if (!isUsed.Contains(input[i]))
                {
                    isUsed.Add(input[i]);
                    currentNumbers[depth] = input[i];

                    GeneratePermutations(depth + 1, input, currentNumbers, isUsed);
                    isUsed.Remove(input[i]);
                }
            }
        }
    }
}