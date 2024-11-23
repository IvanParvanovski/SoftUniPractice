namespace Ex6CombinationsWithoutRepetition
{
    public class Program
    {
        public static int fullIterations = 0;

        public static void Main(string[] args)
        {
            char[] chars = new char[] { 'A', 'B', 'C' };
            int spots = 2;
            char[] currentChars = new char[spots];
            HashSet<char> isUsed = new HashSet<char>();

            GenerateCombinations(0, 2, chars, currentChars, isUsed);
        }

        public static void GenerateCombinations(int depth, int spots, char[] input, char[] currentChars, HashSet<char> isUsed)
        {
            if (depth == spots)
            {
                Console.WriteLine(string.Join(" ", currentChars));
                return;
            }

            for (int i = fullIterations; i < input.Length; i++)
            {
                char symbol = input[i];

                if (!isUsed.Contains(symbol))
                {
                    currentChars[depth] = symbol;
                    isUsed.Add(symbol);

                    GenerateCombinations(depth + 1, spots, input, currentChars, isUsed);
                    isUsed.Remove(symbol);

                    if (depth == 0)
                    {
                        fullIterations += 1;
                    }
                }
                
            }
        }
    }
}