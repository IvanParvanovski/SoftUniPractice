using System;
using System.Linq;

namespace Ex25
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = Console.ReadLine()?.Split(',');
            foreach (string word in words.OrderBy(x => x))
                Console.WriteLine(word);
        }
    }
}