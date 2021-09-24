using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex1Names
{
    class Program
    {
        static void Main(string[] args)
        {
            int namesCount = int.Parse(Console.ReadLine());
            List<string> names = new List<string>();
            
            for (int i = 0; i < namesCount; i++)
            {
                names.Add(Console.ReadLine());    
            }
            
            Console.WriteLine(string.Join("\n", names.OrderBy(x => x)));
        }
    }
}