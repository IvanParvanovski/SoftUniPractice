using System;

namespace Ex21
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // My name is Esmeralda. Today is Christmas Eve and my dad and mam are next to me.
            
            // Output:
            // Eve
            // dad
            // mam
            
            // Read user's input
            string[] words = Console.ReadLine()?.Split();
            
            // Print if the word is the same as reversed
            foreach (string word in words)
                if (String.Equals(word, ReverseString(word), StringComparison.CurrentCultureIgnoreCase))
                    Console.WriteLine(word);
        }
        private static string ReverseString(string word)
        {
            // Reverse the word
            
            char[] reversedWord = word.ToCharArray();
            Array.Reverse(reversedWord);
            return new string(reversedWord);
        }
    }
}