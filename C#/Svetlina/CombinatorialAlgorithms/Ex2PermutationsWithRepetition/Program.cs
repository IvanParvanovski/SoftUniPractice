namespace Ex2PermutationsWithRepetitions
{
    public class Program
    {
        public static void Main(string[] args)
        {
            HashSet<char> isUsed = new HashSet<char>();
            char[] chars = new char[] { 'A', 'B', 'C' };

            char[] currentChars = new char[chars.Length];
            GeneratePermutations(0, chars, currentChars, isUsed);

        }

        private static void GeneratePermutations(int depth, char[] chars, char[] currentChars, HashSet<char> isUsed)
        {
            if (depth == chars.Length)
            {
                Console.WriteLine(new string(currentChars));
                return;
            }

            for (int i = 0; i < chars.Length; i++)
            {
                currentChars[depth] = chars[i];
                GeneratePermutations(depth + 1, chars, currentChars, isUsed);
            }
        }
    }
}