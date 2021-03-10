using System;
using System.Text;

namespace Ex4TextFilter
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = Console.ReadLine()?.Split(", ");
            string text = Console.ReadLine();
            Console.WriteLine(TextFilter(words, text));
        }

        private static string TextFilter(string[] words, string text)
        {
            StringBuilder result = new StringBuilder();
            result.Append(text);
            foreach (string word in words)
                result.Replace(word, GetStars(word));
            return result.ToString();
        }

        private static string GetStars(string word)
        {
            StringBuilder stars = new StringBuilder();
            foreach (char _ in word)
                stars.Append('*');
            return stars.ToString();
        }
    }
}