using System;
using System.Linq;

namespace Ex25
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // Ivan,Microsoft,Apple,Juice
            
            // Output:
            // Apple
            // Ivan
            // Juice
            // Microsoft

            // Read the words and split them by comma
            string[] words = Console.ReadLine()?.Split(',');
            
            // Print the words alphabetically
            foreach (string word in words!.OrderBy(x => x))
                Console.WriteLine(word);
        }
    }
}