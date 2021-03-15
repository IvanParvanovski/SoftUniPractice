using System;
using System.Linq;

namespace Ex2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(string.Join("",
                        Console.ReadLine().Reverse()));
        }
    }
}