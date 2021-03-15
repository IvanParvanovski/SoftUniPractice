using System;

namespace Ex4
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(string.Join('-',@"a\b\c".Split("\\")));
        }
    }
}