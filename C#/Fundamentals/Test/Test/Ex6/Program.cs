using System;
using System.Linq;

namespace Ex6
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] elements1 = Console.ReadLine()!.Split();
            string[] elements2 = Console.ReadLine()!.Split();
            Console.WriteLine(String.Join(' ', elements1.Intersect(elements2)));
        }
    }
}