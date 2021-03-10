using System;

namespace Ex2
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = Console.ReadLine()?.Split();
            string firstWord = words?[0];
            string secondWord = words?[1];

            int firstWordTotal = GetWordTotal(firstWord); 
            int secondWordTotal = GetWordTotal(secondWord);

            int result;
            if (firstWord.Length > secondWord.Length || firstWord.Length < secondWord.Length)
                result = firstWordTotal + secondWordTotal;
            else
                result = firstWordTotal * secondWordTotal;
            
            Console.WriteLine(result);
        }

        private static int GetWordTotal(string word)
        {
            int total = 0;
            foreach (char symbol in word)
                total += symbol;
            return total;
        }
    }
}