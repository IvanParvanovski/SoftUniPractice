using System;
using System.Linq;

namespace Ex2
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input: introduction
            
            // Output: noitcudortni

            // Read string and reverse it.
            Console.WriteLine(string.Join("",
                         Console.ReadLine()!.Reverse()));
        }
    }
}