using System;
using System.Linq;

namespace Ex1SomethingInCommon
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] firstSequence = Console.ReadLine()!.Split();
            string[] secondSequence = Console.ReadLine()!.Split();
            Console.WriteLine(string.Join(' ', secondSequence.Intersect(firstSequence)));
        }
    }
}