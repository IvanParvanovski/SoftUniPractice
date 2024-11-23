namespace Ex7CombinationsWithRepetition
{
    public class Program
    {
        public static int fullIterations = 0;

        public static void Main(string[] args)
        {
            char[] chars = new char[] { 'A', 'B', 'C' };
            int spots = 2;
            char[] currentChars = new char[spots];

            GenerateCombinations(0, 2, chars, currentChars);
        }

        public static void GenerateCombinations(int depth, int spots, char[] input, char[] currentChars)
        {
            if (depth == spots)
            {
                Console.WriteLine(string.Join(" ", currentChars));
                return;
            }

            for (int i = fullIterations; i < input.Length; i++)
            {
                currentChars[depth] = input[i];
                GenerateCombinations(depth + 1, spots, input, currentChars);
                if (depth == 0)
                {
                    fullIterations += 1;
                }
            }
        }
    }
}