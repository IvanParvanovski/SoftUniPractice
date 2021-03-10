using System;
using System.Linq;

namespace Ex1EncryptSortAndPrintArray
{
    class Program
    {
        static void Main(string[] args)
        {
            int wordsCount = Int32.Parse(Console.ReadLine());
            int[] wordsValues = new int[wordsCount];
            for (int i = 0; i < wordsCount; i++)
            {
                string word = Console.ReadLine();
                int wordValue = 0;
                foreach (char symbol in word)
                {
                    if (IsVowel(symbol))
                        wordValue += symbol * word.Length;
                    else
                        wordValue += (int)(symbol / word.Length);
                }
                wordsValues[i] = wordValue;
            }
            Array.Sort(wordsValues);
            foreach (int wordValue in wordsValues)
                Console.WriteLine(wordValue);
        }
        private static bool IsVowel(char symbol)
        {
            char[] vowels = { 'a', 'e', 'i', 'o', 'u' };
            return vowels.Contains(symbol);
        }
    }
}
