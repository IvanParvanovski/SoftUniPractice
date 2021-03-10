using System;

namespace Ex4ReverseArrayOfStrings
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] symbols = Console.ReadLine()
                               .Split(" ");

            Array.Reverse(symbols);
            Console.WriteLine(string.Join(' ', symbols));
        }
    }
}
