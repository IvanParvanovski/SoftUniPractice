using System;
using System.Linq;

namespace Ex2CommonElements
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] firstArrayElements = Console.ReadLine().Split();
            string[] secondArrayElements = Console.ReadLine().Split();
            string[] result = firstArrayElements.Intersect(secondArrayElements).ToArray();

            Console.WriteLine(string.Join(' ', result));
        }
    }
}
