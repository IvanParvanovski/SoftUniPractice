using System;
using System.Linq;

namespace Ex14
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = Console.ReadLine()?.Split();
            words = words.Reverse().ToArray();
            Console.WriteLine(String.Join(' ', words));
        }
    }
}