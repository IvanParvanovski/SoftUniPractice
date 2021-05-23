using System;
using System.Linq;

namespace Ex7
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] elements = Console.ReadLine()!.Split("|")
                                                   .Reverse()
                                                   .ToArray();
            
            foreach (string element in elements)
            {
                string[] currentSequence = element.Split(' ', StringSplitOptions.RemoveEmptyEntries);
                if (currentSequence.Length > 0)
                    Console.Write(String.Join(' ', currentSequence) + ' ');
            }
            
        }
    }
}