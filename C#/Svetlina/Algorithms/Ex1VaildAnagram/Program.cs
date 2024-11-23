namespace Anagram
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var firstStr = "anagram";
            var secondStr = "nagaram";

            Console.WriteLine(IsAnagram(firstStr, secondStr));
            Console.WriteLine(IsAnagram("rat", "car"));


        }

        public static bool IsAnagram(string firstStr, string secondStr)
        {
            var symbolDict = new Dictionary<char, int>();


            foreach (char symbol in firstStr)
            {
                if (!symbolDict.ContainsKey(symbol))
                {
                    symbolDict[symbol] = 0;
                }

                symbolDict[symbol] += 1;
            }

            foreach (char symbol in secondStr)
            {
                if (!symbolDict.ContainsKey(symbol))
                {
                    return false;
                }

                symbolDict[symbol] -= 1;
            }

            return symbolDict.Values.All(value => value == 0);
        }
    }
}
