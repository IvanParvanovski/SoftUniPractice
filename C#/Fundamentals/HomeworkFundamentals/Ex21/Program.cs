using System;
using System.Linq;

namespace Ex21
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = Console.ReadLine()?.Split();
            foreach (string word in words)
                if (word == ReverseString(word))
                    Console.WriteLine(word);
        }
        private static string ReverseString(string word)
        {
            char[] reversedWord = word.ToCharArray();
            Array.Reverse(reversedWord);
            return new string(reversedWord);
        }
    }
}