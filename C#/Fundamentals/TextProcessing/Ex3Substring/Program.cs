using System;
using System.Text;

namespace Ex3Substring
{
    class Program
    {
        static void Main(string[] args)
        {
            string word = Console.ReadLine();
            string text = Console.ReadLine();
            Console.WriteLine(SubstringWords(word, text));
        }
        private static string SubstringWords(string word, string text)
        {
            StringBuilder result = new StringBuilder();
            result.Append(text);
            
            int n = word.Length;

            while (true)
            {
                int index = result.ToString()   
                                  .IndexOf(word, StringComparison.OrdinalIgnoreCase);
                
                if (index == -1)
                    break;
                
                result.Remove(index, n);
            }

            return result.ToString();
        }
    }
}