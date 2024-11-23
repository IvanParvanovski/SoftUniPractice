using System;
using System.Threading;

namespace Ex2HotAndCold2
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            var coldThread = new Thread(PrintCold);
            coldThread.Start();
            coldThread.Join();

            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine("Hot");
                Thread.Sleep(200);
            }
        }

        static void PrintCold()
        {
            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine("Cold");
                Thread.Sleep(200);
            }

        }
    }
}
