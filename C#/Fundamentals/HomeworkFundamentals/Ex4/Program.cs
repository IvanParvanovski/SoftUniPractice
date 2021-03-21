using System;

namespace Ex4
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input: a\b\c
            
            // Output: a-b-c
            
            Console.WriteLine(string.Join('-',@"a\b\c".Split("\\")));
        }
    }
}