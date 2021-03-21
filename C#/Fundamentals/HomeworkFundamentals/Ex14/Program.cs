using System;
using System.Linq;

namespace Ex14
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // C# is not C++ and PHP is not Delphi
            
            // Output:
            // Delphi not is PHP and C++ not is C#
            
            // Reverse the words
            
            string[] words = Console.ReadLine()?.Split();
            words = words.Reverse().ToArray();
            Console.WriteLine(String.Join(' ', words));
        }
    }
}