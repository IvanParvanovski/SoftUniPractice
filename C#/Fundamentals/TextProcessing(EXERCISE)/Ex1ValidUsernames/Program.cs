using System;

namespace Ex1ValidUsernames
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = Console.ReadLine()?.Split(", ");
            foreach (string word in words)
            {
                if (word.Length > 16 || word.Length < 3)
                    continue;
                
                bool isValid = true;
                foreach (char symbol in word)
                    if (!(Char.IsDigit(symbol) || Char.IsLetter(symbol)) || Char.IsSeparator(symbol))
                    {
                        isValid = false;
                        break;
                    }
                
                if (isValid)
                    Console.WriteLine(word);
            }
        }
    }
}