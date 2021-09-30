using System;
using System.Collections.Generic;

namespace Ex1RepeatedNames
{
    class Program
    {
        static void Main(string[] args)
        {
            HashSet<string> names = new HashSet<string>();
            int namesCount = int.Parse(Console.ReadLine());

            for (int i = 0; i < namesCount; i++)
            {
                string name = Console.ReadLine();
                names.Add(name);
                
            }

            Console.WriteLine(string.Join("\n", names));
        }
    }
}