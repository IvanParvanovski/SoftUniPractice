using System;
using System.Collections.Generic;
using System.Linq;

namespace Demo1
{
    class Program
    {
        static void Main(string[] args)
        {
            int me;
            bool c = int.TryParse(Console.ReadLine(), out me);

            Console.WriteLine(me);
            Console.WriteLine(c);
        }

        


    }
}
