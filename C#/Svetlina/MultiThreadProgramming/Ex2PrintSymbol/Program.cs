using System;
using System.Threading;

namespace Ex2PrintSymbol
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Thread thread = new Thread(() => Go('O'));
            thread.Start();

            Go('X');
                
        }

        static void Go(char symbol)
        {
            for (int i = 0; i < 450; i++)
            {
                Console.Write(symbol);
            }
        }
    }
}
