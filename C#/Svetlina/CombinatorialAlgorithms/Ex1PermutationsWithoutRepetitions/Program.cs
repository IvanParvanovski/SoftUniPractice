namespace Ex1PermutationsWithoutRepetitions
{
    public class Program
    {
        public static void Main(string[] args)
        {
            HashSet<char> isUsed = new HashSet<char>();
            char[] chars = new char[] { 'X', 'Y', 'Z' };
            char[] currentChars = new char[chars.Length];
            GeneratePermutations(0, chars, currentChars, isUsed);

        }

        private static void GeneratePermutations(int depth, char[] input, char[] currentChars, HashSet<char> isUsed)
        {
            if (depth == input.Length)
            {
                Console.WriteLine(string.Join(" ", currentChars));
            }

            for (int i = 0; i < input.Length; i++)
            {
                if (!isUsed.Contains(input[i]))
                {
                    isUsed.Add(input[i]);
                    currentChars[depth] = input[i];

                    GeneratePermutations(depth + 1, input, currentChars, isUsed);
                    isUsed.Remove(input[i]);
                }
            }
        }
    }
}