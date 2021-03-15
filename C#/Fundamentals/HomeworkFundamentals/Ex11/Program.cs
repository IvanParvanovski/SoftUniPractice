using System;
using System.Text;

namespace Ex11
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] bannedWords = Console.ReadLine()?.Split(',');
            StringBuilder text = new StringBuilder(Console.ReadLine());
            
            foreach (string bannedWord in bannedWords)
                text.Replace(bannedWord, new string('*', bannedWord.Length));
            
            Console.WriteLine(text);
        }
    }
}