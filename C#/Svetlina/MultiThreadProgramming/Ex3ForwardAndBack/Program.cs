using System;
using System.Collections.Generic;
using System.Threading;

namespace Ex3ForwardAndBack
{
    class MainClass
    {
        public static List<string> symbols = new List<string>() { "o", "o", "x", "o", "o" };

        public static void Main(string[] args)
        {
            char symbol = 'f';
            Thread firstThread = new Thread(Forward);
            firstThread.Start();

            Thread secondThread = new Thread(Back);
            secondThread.Start();

        }

        static void Forward()
        {
            Thread.Sleep(50);
            symbols[4] = "f";
            Console.WriteLine(string.Join(" ", symbols));
        }

        static void Back()
        {
            Thread.Sleep(100);
            symbols[4] = "o";
            symbols[1] = "b";
            Console.WriteLine(string.Join(" ", symbols));
        }
    }
}
