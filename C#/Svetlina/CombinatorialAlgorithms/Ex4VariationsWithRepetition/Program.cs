namespace Ex4VariationsWithRepetitions
{
    public class Program
    {
        public static void Main(string[] args)
        {
            char[] chars = new char[] { 'A', 'B', 'C' };
            int spots = 2;
            char[] currentChars = new char[spots];

            GenerateVariation(0, spots, chars, currentChars);
        }

        private static void GenerateVariation(int depth, int spots, char[] input, char[] currentChars)
        {
            if (depth == spots)
            {
                Console.WriteLine(string.Join(" ", currentChars));
                return;
            }

            for (int i = 0; i < input.Length; i++)
            {
                currentChars[depth] = input[i];
                GenerateVariation(depth + 1, spots, input, currentChars);
            }
        }
    }
}
