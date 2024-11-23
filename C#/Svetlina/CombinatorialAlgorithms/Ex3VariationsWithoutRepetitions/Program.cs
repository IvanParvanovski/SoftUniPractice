namespace Ex3VariationsWithoutRepetitions
{
    public class Program
    {
        public static void Main(string[] args)
        {
            HashSet<char> isUsed = new HashSet<char>();
            char[] chars = new char[] { 'A', 'B', 'C' };
            int spots = 2;
            char[] currentChars = new char[spots];

            GenerateVariation(0, spots, chars, currentChars, isUsed);
        }

        private static void GenerateVariation(int depth, int spots, char[] input, char[] currentChars, HashSet<char> isUsed)
        {
            if (depth == spots)
            {
                Console.WriteLine(string.Join(" ", currentChars));
                return;
            }

            for (int i = 0; i < input.Length; i++)
            {
                if (!isUsed.Contains(input[i]))
                {
                    isUsed.Add(input[i]);
                    currentChars[depth] = input[i];

                    GenerateVariation(depth + 1, spots, input, currentChars, isUsed);
                    isUsed.Remove(input[i]);
                }
            }
        }
    }
}
